from flask_cors import cross_origin
from flask import request
from app import app
from database import user_actions_table


@app.route("/actions/<string:user_id>", methods=['GET'])
@cross_origin()
def get_user_action(user_id):
    users_actions = user_actions_table.UsersActionTable().get_action_by_userId(user_id)
    if users_actions:
        return {'message': users_actions}
    else:
        return {'message': 'User doesnt have actions'}


@app.route("/actions/family/<string:family_id>", methods=['GET'])
@cross_origin()
def get_family_action(family_id):
    result = {}
    users_actions = user_actions_table.UsersActionTable().get_all_family_actions(family_id)
    for user_action in users_actions:
        if result.get(user_action[0]):
            result[user_action[0]].append(
                {
                    'user_id': user_action[0],
                    'action_id': user_action[1],
                    'action_name': user_action[2],
                    'action_price': user_action[3],
                }
            )
        else:
            result[user_action[0]] = []
            result[user_action[0]] = [
                {
                    'user_id': user_action[0],
                    'action_id': user_action[1],
                    'action_name': user_action[2],
                    'action_price': user_action[3],
                }
            ]

    return result


@app.route("/actions/", methods=['POST', 'OPTIONS'])
@cross_origin()
def add_action():
    userId = request.json.get('email')
    productName = request.json.get('productName')
    price = request.json.get('price')
    try:
        user_actions_table.UsersActionTable().add_user_actions(userId, productName, price)
        return {'message': 'Inserted successfully'}
    except:
        return {'message': 'error'}
