from flask_cors import cross_origin
from flask import request
from app import app
from database import user_amount_table


@app.route("/amount/<string:user_id>", methods=['GET'])
@cross_origin()
def get_user_amount(user_id):
    users_amount = user_amount_table.UsersAmountTable().get_user_amount(user_id)
    if users_amount:
        return {'message': users_amount}
    else:
        return {'message': 'User doesnt have actions'}


@app.route("/amount/family/<string:family_id>", methods=['GET'])
@cross_origin()
def get_family_amount(family_id):
    result = {}
    users_amount = user_amount_table.UsersAmountTable().get_all_family_amount(family_id)
    for user_amount in users_amount:
        if result.get(user_amount[0]):
            result[user_amount[0]].append(
                {
                    'user_id': user_amount[0],
                    'user_bank_account': user_amount[1],
                    'user_amount': user_amount[2],
                }
            )
        else:
            result[user_amount[0]] = []
            result[user_amount[0]] = [
                {
                    'user_id': user_amount[0],
                    'user_bank_account': user_amount[1],
                    'user_amount': user_amount[2],
                }
            ]

    return result


@app.route("/amount/", methods=['POST', 'OPTIONS'])
@cross_origin()
def add_amount():
    user_id = request.json.get('email')
    bank_number = request.json.get('bankNumber')
    amount = request.json.get('amount')
    try:
        user_amount_table.UsersAmountTable().add_amount(user_id, bank_number, amount)
        return {'message': 'Inserted successfully'}
    except:
        return {'message': 'error'}


@app.route("/amount/<string:user_id>", methods=['PUT', 'OPTIONS'])
@cross_origin()
def update_amount(user_id: str):
    amount = request.json.get('newAmount')
    try:
        user_amount_table.UsersAmountTable().update_amount(user_id, amount)
        return {'message': 'Inserted successfully'}
    except:
        return {'message': 'error'}
