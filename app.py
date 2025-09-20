import os
import logging
import requests
import google.generativeai as genai
from flask import Response
from twilio.twiml.messaging_response import MessagingResponse

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("misinfox")

# Env keys (set these in Cloud Functions config; do NOT hardcode)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CX = os.getenv("GOOGLE_CX")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    logger.warning("Gemini API key not set.")


FORWARD_WORDS_THRESHOLD = 15

def do_google_search(query):
    """Return a short formatted string from Google Custom Search (top result)."""
    if not GOOGLE_API_KEY or not GOOGLE_CX:
        logger.warning("Google keys not set.")
        return "⚠️ Search keys not configured."

    try:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {"key": GOOGLE_API_KEY, "cx": GOOGLE_CX, "q": query, "num": 2}
        r = requests.get(url, params=params, timeout=8)
        r.raise_for_status()
        data = r.json()
        items = data.get("items", [])
        if not items:
            return f"😕 No results found for: {query}"
        top = items[0]
        title = top.get("title", "Untitled")
        snippet = top.get("snippet", "")
        link = top.get("link", "")
        return f"🔎 {title}\n{snippet}\n\n🔗 {link}"
    except Exception as e:
        logger.exception("Google search error")
        return f"⚠️ Error during search: {e}"

def is_forward_like(text: str) -> bool:
    if not text:
        return False
    if len(text.split()) >= FORWARD_WORDS_THRESHOLD:
        return True
    low = text.lower()
    if "http://" in low or "https://" in low:
        return True
    if low.startswith("fw:") or low.startswith("fwd:"):
        return True
    if low.count("\n") >= 2:
        return True
    return False

def format_with_gemini(claim: str, search_result: str) -> str:
    """
    Use Gemini to format and improve the fact-check reply.
    """
    if not GEMINI_API_KEY:
        return f"📰 Fact-check for: {claim}\n\n{search_result}"

    try:
        prompt = f"""
        You are MisinfoX, a fact-checking assistant.
        Keeps an eye on what kind of misinformation is trending, so we know what’s circulating the most.
        The user asked to verify: "{claim}".

        Here is the raw search result:
        {search_result}

        Please:
        - Give a clear verdict (true, false, misleading, or uncertain).
        - Provide a short, user-friendly explanation (make sure you keep complete content within 1550characters long, not more than that), especially telling as to how the claim is misleading/false/uncertain incase any.
        - Show atleast 2 trusted source with its link.
        - Keep it concise for WhatsApp.
        
        """

        model = genai.GenerativeModel("gemini-2.0-flash")
        #model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip() if response and response.text else f"📰 Fact-check for: {claim}\n\n{search_result}"
    except Exception as e:
        logger.exception("Gemini formatting failed")
        return f"📰 Fact-check for: {claim}\n\n{search_result}"


# Cloud Function entry point — Twilio will call this
def misinfox_bot_entry(request):
    try:
        # Log everything useful for debugging
        try:
            headers = dict(request.headers)
        except Exception:
            headers = {"note": "could not read headers"}
        try:
            form = dict(request.form)
        except Exception:
            form = {"note": "could not read form"}
        try:
            values = dict(request.values)
        except Exception:
            values = {"note": "could not read values"}

        logger.info("Incoming request headers: %s", headers)
        logger.info("Incoming request form: %s", form)
        logger.info("Incoming request values: %s", values)

        # Twilio usually sends Body in request.values or request.form
        body = request.values.get("Body") or request.form.get("Body") or ""
        if body is None:
            body = ""
        incoming_raw = str(body).strip()
        lower_msg = incoming_raw.lower()

        resp = MessagingResponse()

        # Greetings
        if lower_msg in ("hi", "hello"):
            resp.message("👋 Hello! I’m MisinfoX — type `help` or `verify <claim>` to check something.")
            return Response(str(resp), mimetype="application/xml", status=200)

        # Help
        elif lower_msg in ("help", "menu"):
            resp.message(
                "📋 MisinfoX commands:\n"
                "• `verify <claim>` — I will search and return top sources.\n"
                "• Forward a long message (or paste a long text) — I auto-check.\n"
                "• Try: verify the earth is flat"
            )
            return Response(str(resp), mimetype="application/xml", status=200)

        # Explicit verify (allow both "verify x" and "/verify x")
        if lower_msg.startswith("verify") or lower_msg.startswith("/verify"):
            # preserve original casing for search but strip command
            claim = incoming_raw
            if lower_msg.startswith("/verify"):
                claim = incoming_raw[len("/verify"):].strip()
            else:
                claim = incoming_raw[len("verify"):].strip()

            if not claim:
                resp.message("⚠️ Please provide text after `verify`. Example: verify The earth is flat")
                return Response(str(resp), mimetype="application/xml", status=200)

            # run google search (simple for now)
            results = do_google_search(claim)
            final_reply = format_with_gemini(claim, results)
            resp.message(final_reply)

            return Response(str(resp), mimetype="application/xml", status=200)

        # Forwarded-like auto-check
        if is_forward_like(incoming_raw):
            results = do_google_search(incoming_raw)
            resp.message(f"📨 Detected forwarded/long message — quick check:\n\n{results}")
            return Response(str(resp), mimetype="application/xml", status=200)

        # Fallback
        resp.message("🤖 I didn’t understand. Type `help` or `verify <claim>`.")
        return Response(str(resp), mimetype="application/xml", status=200)

    except Exception as e:
        logger.exception("Exception in handler")
        fallback = MessagingResponse()
        fallback.message("⚠️ Internal error. Please try again.")
        return Response(str(fallback), mimetype="application/xml", status=200)
