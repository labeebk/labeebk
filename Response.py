from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

import twilio
import twilio.rest
import twilio.twiml
import Database
from twilio.rest import TwilioRestClient

# Login Details
account_sid = "ACb0aa3c45f351b6b70eafe9b9f9746c7b"
auth_token = "c1a17eb5b826309f2fe48be50f618655"
client = TwilioRestClient(account_sid, auth_token)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
