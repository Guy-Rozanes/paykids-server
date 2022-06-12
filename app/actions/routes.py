from flask_cors import cross_origin
from flask import request
from app import app
from app.paybox_client.routes import PayboxConnection
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
                    'action_seen': user_action[4],
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
                    'action_seen': user_action[4],
                }
            ]

    return result


@app.route("/actions/", methods=['POST', 'OPTIONS'])
@cross_origin()
def add_action():
    userId = request.json.get('email')
    product_name = request.json.get('productName')
    if not product_name:
        return {'message': 'Please Enter Product Name'}
    price = request.json.get('price')
    group_id = request.json.get('paybox_group')
    if not price:
        return {'message': 'Please Enter Price'}
    else:
        if not price.isdecimal():
            return {'message': 'Please Enter a Real Price'}
    try:
        user_actions_table.UsersActionTable().add_user_actions(userId, product_name, price)
        return {'message': 'Inserted successfully'}
    except:
        return {'message': 'error'}


@app.route("/actions/<string:action_id>", methods=['PUT', 'OPTIONS'])
@cross_origin()
def mark_action_as_read(action_id):
    try:
        user_actions_table.UsersActionTable().update_seen_to_true(action_id)
        return {'message': 'Inserted successfully'}
    except:
        return {'message': 'error'}


@app.route("/actions/sync", methods=['POST', 'OPTIONS'])
@cross_origin()
def sync_from_paybox():
    paybox_id = request.json.get('paybox_id')
    username = request.json.get('username')
    password = request.json.get('password')
    try:
        return PayboxConnection(username, password, paybox_id).get_group_bills()
    except:
        return {'message': 'error'}
