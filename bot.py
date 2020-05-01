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

    if 'dog' or 'puppy' in incoming_msg:
        r = requests.get('https://dog.ceo/api/breeds/image/random')
        if r.status_code == 200:
            data = r.json()
            dog = data["message"]
        else:
            dog = "Sorry, no dogs here!"
        
        msg.media(dog)    
        responded = True

    if 'hobby' in incoming_msg:
        hobbies = open('hobbies.txt').read().splitlines()
        hobby =random.choice(hobbies)
        msg.body(hobby)
        responded = True

    if not responded:
        msg.body("Sorry, the code is busted!")
    return str(resp)

if __name__ == "__main__":
    app.run() 