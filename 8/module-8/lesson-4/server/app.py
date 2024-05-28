from decimal import Decimal, getcontext
from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/pi')
def index():
    length = request.args.get('length')
    pi = calcPi(int(length))
    return jsonify(pi=pi)

def calcPi(length):
    getcontext().prec = length
    pi = sum(1 / Decimal(16) ** k *
             (Decimal(4) / (8 * k + 1) -
              Decimal(2) / (8 * k + 4) -
              Decimal(1) / (8 * k + 5) -
              Decimal(1) / (8 * k + 6)) for k in range(100))
    return pi

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port='8080')