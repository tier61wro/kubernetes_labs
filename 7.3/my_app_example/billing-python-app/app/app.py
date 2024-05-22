import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Transactions(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.String(100))
    amount = db.Column(db.Integer)

    def __init__(self, client_id, amount):
        self.client_id = client_id
        self.amount = amount

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'client_id': self.client_id,
            'amount': self.amount,
        }


@app.route("/ping")
def hello():
    with app.app_context():
        return "pong"


@app.route("/add", methods=['POST'])
def add_transaction():
    with app.app_context():
        client_id = request.args.get('client_id')
        amount = request.args.get('amount')
        try:
            transaction = Transactions(
                client_id=client_id,
                amount=amount,
            )
            db.session.add(transaction)
            db.session.commit()
            return "Transaction added. transaction id={}".format(transaction.id)
        except Exception as e:
            return (str(e))


@app.route("/getall")
def get_all():
    with app.app_context():
        try:
            transactions = Transactions.query.all()
            return jsonify([e.serialize() for e in transactions])
        except Exception as e:
            return (str(e))


@app.route("/get/<id_>")
def get_by_id(id_):
    with app.app_context():
        try:
            transaction = Transactions.query.filter_by(id=id_).first()
            return jsonify(transaction.serialize())
        except Exception as e:
            return (str(e))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run("0.0.0.0", 8080)
