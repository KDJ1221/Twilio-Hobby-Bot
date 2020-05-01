from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import random

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'quote' in incoming_msg:
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = "Could not give you a quote"
        msg.body(quote)
        responded = True
    
    if 'cat' in incoming_msg:
        msg.media('https://cataas.com/cat')
        responded = True

    if 'hobby' in incoming_msg:
        hobbies = open('hobbies.txt').read().splitlines()
        hobby =random.choice(hobbies)
        msg.body(hobby)
        responded = True

    if not responded:
        msg.body("Generic response of how you're wrong")
    return str(resp)

if __name__ == "__main__":
    app.run() 