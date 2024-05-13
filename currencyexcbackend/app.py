from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json
import requests
import random
      
app = Flask(__name__)
cors = CORS(app, origins=['http://localhost:4200'])
app.config['CORS_HEADERS'] = 'application/json'

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/api/exchange')
@cross_origin()
def api1s():
    fromCurrency = request.args.get("from")
    toCurrency = request.args.get("to")
    amount = float( request.args.get("amount"))
    rate = 1.0
    if fromCurrency == 'USD' and toCurrency == 'SOL':
        rate = 3.75
    if fromCurrency == 'SOL' and toCurrency == 'USD':
        rate = 1.0 / 3.75
    return jsonify({'amount': round(amount * rate, 2)})
#http://127.0.0.1:5000/api1

if __name__ == '__main__':
    app.run(debug=True, threaded=False, port=5000)
