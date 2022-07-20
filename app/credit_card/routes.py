from flask_cors import cross_origin
from flask import request
from app import app
from database import users_card_table


@app.route("/user/card/", methods=['POST', 'OPTIONS'])
@cross_origin()
def insert_card():
    email = request.json.get('userId')
    last4 = request.json.get('last4')
    exp = request.json.get('exp')
    try:
        users_card_table.UsersCardTable().insert_card(email, last4, exp)
        return {'message': 'inserted succesfully'}
    except Exception:
        return {'message': 'Can not insert card'}


@app.route("/user/card/<string:email>", methods=['GET'])
@cross_origin()
def get_cards(email):
    card = users_card_table.UsersCardTable().get_card_by_email(email)
    if card:
        return {'message': card}
    else:
        return {'message': 'User do not have any card'}


@app.route("/user/card/", methods=['DELETE'])
@cross_origin()
def delete_cards():
    last4 = request.json.get('last4')
    exp = request.json.get('exp')
    try:
        users_card_table.UsersCardTable().delete_card(last4, exp)
        return {'message': 'Card Deleted'}
    except Exception:
        return {'message': 'Cant delete'}
