from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/pybot')
def pybot():
    user_code = request.form.get('Body')
    resp = MessagingResponse()
    send = resp.message()
    send.body(exec(user_code))

if __name__ == '__main__':
    app.run(debug=True, port=4000)