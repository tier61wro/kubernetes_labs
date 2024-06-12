import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    serverMessage = os.getenv("SERVER_MESSAGE")
    return jsonify(message=serverMessage)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port='8080')
