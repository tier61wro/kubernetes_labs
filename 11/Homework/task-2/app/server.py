import random
from datetime import datetime
from threading import Timer

from flask import Flask, jsonify

app = Flask(__name__)

message = "ok"
response = 200
random.seed(datetime.now())
time_to_shutdown = random.randint(0, 60)
time_to_respawn = random.randint(time_to_shutdown, time_to_shutdown + 30)


def shutdown():
    print("stopping...")
    listOfGlobals = globals()
    listOfGlobals['message'] = "server error"
    listOfGlobals['response'] = 502


def respawn():
    print("respawning...")
    listOfGlobals = globals()
    listOfGlobals['message'] = "ok"
    listOfGlobals['response'] = 200


@app.route('/health')
def health():
    return jsonify(status=message), response


@app.route('/')
def index():
    dateNow = datetime.now().strftime("%m/%d/%Y-%H:%M:%S")
    if message == "ok":
        return jsonify(date=dateNow, version="t2")
    else:
        return jsonify(date="timed-out", version="t2")


if __name__ == '__main__':
    timer_shutdown = Timer(time_to_shutdown, shutdown)
    timer_shutdown.start()
    timer_respawn = Timer(time_to_respawn, respawn)
    timer_respawn.start()
    app.run(debug=True, host='0.0.0.0', port='8080')
