from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "hello" in incoming_msg:
        msg.body("Hello 👋, this is MisinfoX WhatsApp bot. Send me any news/claim and I’ll help check it.")
    else:
        msg.body("Got it! I’ll soon verify this claim for you.")
    
    return str(resp)

# Google Cloud Functions entry point
def misinfox_bot(request):
    with app.test_request_context(
        path=request.path,
        base_url=request.base_url,
        method=request.method,
        data=request.get_data(),
        headers=request.headers
    ):
        return app.full_dispatch_request()
