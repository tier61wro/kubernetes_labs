import random
from datetime import datetime
from threading import Timer

from flask import Flask, jsonify

app = Flask(__name__)

message = "ok"
response = 200
random.seed(datetime.now())
time_to_shutdown = random.randint(0, 300)


def shutdown():
    print("Terminating...")
    listOfGlobals = globals()
    listOfGlobals['message'] = "server error"
    listOfGlobals['response'] = 502


@app.route('/health')
def health():
    return jsonify(status=message), response


@app.route('/')
def index():
    dateNow = datetime.now().strftime("%m/%d/%Y-%H:%M:%S")
    if message == "ok":
        return jsonify(date=dateNow, version="t1"), response
    else:
        return jsonify(date=message, version="t1"), response


if __name__ == '__main__':
    timer = Timer(time_to_shutdown, shutdown)
    timer.start()
    app.run(debug=True, host='0.0.0.0', port='8080')
