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

FORWARD_WORDS_THRESHOLD = 25

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
    """Detect if text looks like a forwarded/long/chain message."""
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

def format_with_gemini(claim: str, search_result: str, is_forward: bool = False) -> str:
    """
    Use Gemini to format and improve the fact-check reply.
    Adds special prefix if the message was detected as forwarded.
    """
    prefix = "📨 This looks like a forwarded/chain message. Verifying...\n\n" if is_forward else ""

    if not GEMINI_API_KEY:
        return prefix + f"📰 Fact-check for: {claim}\n\n{search_result}"

    try:
        prompt = f"""
        You are MisinfoX — a fact-checking assistant and phishing URL detection bot.  
        Your job is to analyze the given input message and determine whether it contains misinformation or a phishing attempt.  

        If the message includes a URL, always verify and analyze the link whether the link is safe and leads you to a particular page/site or potentially phishing.  

        The user asked to verify: "{claim}"  

                Here is the raw search result: {search_result}  

        Please:  
            - if url present and suspicious then verdict must be "Scam" only
            - Provide a clear verdict: *true*, *false*, *suspicious*, *scam* or *uncertain*.  
            - Along with the verdict, include a confidence score in percentage (e.g., “False — 92% sure”).  
            - Write a short, user-friendly explanation (must stay within **1550 characters**).  
            - If verdict is *false*, *suspicious*, *scam* or *uncertain*, briefly explain *why*.  
            - Cite **at least 2 trusted sources** with valid links.  
            - Keep the tone **concise, neutral, and WhatsApp-friendly**
            - Remember somtimes the mesaages might be true but the links are fake so take a not of that and tell it as well.

        """

        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        return prefix + (response.text.strip() if response and response.text else f"📰 Fact-check for: {claim}\n\n{search_result}")
    except Exception as e:
        logger.exception("Gemini formatting failed")
        return prefix + f"📰 Fact-check for: {claim}\n\n{search_result}"

# Cloud Function entry point — Twilio will call this
def misinfox_bot_entry(request):
    try:
        # Log request info
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

        # Extract message text
        body = request.values.get("Body") or request.form.get("Body") or ""
        if body is None:
            body = ""
        incoming_raw = str(body).strip()
        lower_msg = incoming_raw.lower()

        resp = MessagingResponse()

        # Greetings
        if lower_msg in ("hi", "hello", "hey"):
            resp.message("👋 Hello! I’m MisinfoX — type `help` or `verify <claim>` to check something.")
            return Response(str(resp), mimetype="application/xml", status=200)

        # Help/Menu
        elif lower_msg in ("help", "menu"):
            resp.message(
                "📋 MisinfoX commands:\n"
                "• `verify <claim>` — I will search and return top sources.\n"
                "• Forward a long message (or paste a long text) — I auto-check.\n"
                "• Try: verify the earth is flat"
            )
            return Response(str(resp), mimetype="application/xml", status=200)

        # Explicit verify
        if lower_msg.startswith("verify") or lower_msg.startswith("/verify"):
            claim = incoming_raw
            if lower_msg.startswith("/verify"):
                claim = incoming_raw[len("/verify"):].strip()
            else:
                claim = incoming_raw[len("verify"):].strip()

            if not claim:
                resp.message("⚠️ Please provide text after `verify`. Example: verify The earth is flat")
                return Response(str(resp), mimetype="application/xml", status=200)

            results = do_google_search(claim)
            final_reply = format_with_gemini(claim, results)
            resp.message(final_reply)
            return Response(str(resp), mimetype="application/xml", status=200)

        # Forwarded/long auto-check
        if is_forward_like(incoming_raw):
            results = do_google_search(incoming_raw)
            final_reply = format_with_gemini(incoming_raw, results, is_forward=True)
            resp.message(final_reply)
            return Response(str(resp), mimetype="application/xml", status=200)

        # Fallback
        resp.message("🤖 I didn’t understand. Type `help` or `verify <claim>`.")
        return Response(str(resp), mimetype="application/xml", status=200)

    except Exception as e:
        logger.exception("Exception in handler")
        fallback = MessagingResponse()
        fallback.message("⚠️ Internal error. Please try again.")
        return Response(str(fallback), mimetype="application/xml", status=200)
