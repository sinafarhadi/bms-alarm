from flask import Flask, jsonify, request
import requests
import config

app = Flask(__name__)


@app.route('/')
def main_page():
    '''This is the mail page og the site
    '''
    return 'Hello'


@app.route('/v1/proccess', methods=['POST'])
def proccess():
    """
    This is a call back from kavehnegar
    """

    data = request.form
    sender = data["from"]
    message = data["message"]
    print (f'received {message} from {sender}')

    ret = {"message": "processed"}

    send_sms({sender}, f'hi {sender}')

    return jsonify(ret), 200

def send_sms(receptor, message):
    url = f'https://api.kavenegar.com/v1/{config.kavenegar_API}/sms/send.json'
    data = {"sender": {config.kavenegar_number},
            "receptor": receptor,
            "message": message,
            
            }

    res = requests.post(url, data)
    print(f"message {message} sent to {receptor}. status code is {res.status_code}")

def check_serial():
    pass



if __name__ == "__main__":
    
    app.run("0.0.0.0", 5000)
