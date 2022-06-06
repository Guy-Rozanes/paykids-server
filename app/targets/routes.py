from flask_cors import cross_origin
from flask import request
from app import app
from database import user_target_table


@app.route("/targets/<string:user_id>", methods=['GET'])
@cross_origin()
def get_user_targets(user_id):
    users_targets = user_target_table.UsersTargetsTable().get_target_by_email(user_id)
    if users_targets:
        return {'message': users_targets}
    else:
        return {'message': 'User doesnt have targets'}


@app.route("/family/targets/<string:family_id>", methods=['GET'])
@cross_origin()
def get_family_targets(family_id):
    result = {}
    users_targets = user_target_table.UsersTargetsTable().get_all_family_targets(family_id)
    for user_target in users_targets:
        if result.get(user_target[0]):
            result[user_target[0]].append(
                {
                    'user_id': user_target[0],
                    'target_id': user_target[1],
                    'target_name': user_target[2],
                    'target_price': user_target[3],
                }
            )
        else:
            result[user_target[0]] = []
            result[user_target[0]] = [
                {
                    'user_id': user_target[0],
                    'target_id': user_target[1],
                    'target_name': user_target[2],
                    'target_price': user_target[3],
                }
            ]

    return result


@app.route("/targets/", methods=['POST', 'OPTIONS'])
@cross_origin()
def add_target():
    user_id = request.json.get('email')
    target_name = request.json.get('targetName')
    if not target_name:
        return {'message': 'Please Enter Target Name'}
    price = request.json.get('targetPrice')
    if not price:
        return {'message': 'Please Enter Price'}
    else:
        if not price.isdecimal():
            return {'message': 'Please Enter Real Price'}

    try:
        user_target_table.UsersTargetsTable().add_user_target(user_id, target_name, price)
        return {'message': 'Inserted successfully'}
    except:
        return {'message': 'error'}


@app.route("/targets/<string:target_id>", methods=['DELETE', 'OPTIONS'])
@cross_origin()
def delete_target(target_id):
    user_target_table.UsersTargetsTable().delete_target(target_id)
    return {'message': 'Deleted'}
