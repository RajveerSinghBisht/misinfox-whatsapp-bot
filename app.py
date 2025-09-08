from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.values.get("Body", "").strip()
    sender = request.values.get("From", "")

    print(f"Message from {sender}: {incoming_msg}")

    # Simple reply
    resp = MessagingResponse()
    reply = resp.message(f"Got your message: {incoming_msg}")
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
