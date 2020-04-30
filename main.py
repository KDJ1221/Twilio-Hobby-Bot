from flask import Flask, request
from twilio.twiml.messaging_response import MessagingReponse

app = Flask(_name_)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()

    resp = MessagingReponse()
    msg = resp.message()
    msg.body('this is the response text')
    msg.media(image_url)

    responded = False
    if 'quote' in incoming_msg:
        
        responded = True
    
    if 'cat' in incoming_msg:

        responded = True

    if not responded:
        return "Generic response"
