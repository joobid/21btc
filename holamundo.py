import flask
from two1.wallet import Wallet
from two1.bitserv.flask import Payment
import yaml
import json

app = flask.Flask(__name__)
payment = Payment(app, Wallet())


@app.route('/hello')
@payment.required(5000)
def hello():
    return 'Hello, world'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)