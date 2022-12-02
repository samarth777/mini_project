import sys
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

account_sid = 'ACC_SID' 
auth_token = 'AUTH_TOKEN' 
client = Client(account_sid, auth_token) 

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/pybot',methods=['POST', 'GET'])
def pybot():
    userNo = request.values.get('From')
    usercode = request.values.get('Body')
    original_stdout = sys.stdout
    sys.stdout = open('output.txt', 'w')
    exec(usercode)
    sys.stdout.close()
    sys.stdout = original_stdout
    output = open('output.txt', 'r').read()
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=output,      
                              to=userNo 
                          ) 
    
    return 'None'

if __name__ == '__main__':
    app.run(debug=True)