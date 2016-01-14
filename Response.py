import twilio
import twilio.rest
import twilio.twiml
import Database
from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient

# Login Details
account_sid = "ACb0aa3c45f351b6b70eafe9b9f9746c7b"
auth_token = "c1a17eb5b826309f2fe48be50f618655"
client = TwilioRestClient(account_sid, auth_token)

# number_input = request.values.get('From', None)
number_input = "12899210259"

result = 0

# Number to Name
for x in range(0,len(Database.numbers)):
    if Database.numbers[x] in number_input:
        name_output = Database.names[x]
        result = 2
        break
    else:
        result = 1


if result is 1:      # Random Number

    message = client.messages.create(to=number_input, from_="12898125434",
                                        body="Hello, I am currently invite only.")

elif result is 2:    # Known Number

    message = client.messages.create(to=number_input, from_="12898125434",
                                     body="Hey " + name_output + " this is Bot Labeeb. I cannot take any messages at the moment.")

