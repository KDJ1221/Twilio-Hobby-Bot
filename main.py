from flask import Flask

app = Flask(_name_)

@app.route('/bot', methods=['POST'])
def bot():
    #webhook
