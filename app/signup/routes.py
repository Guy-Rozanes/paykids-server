from flask_cors import cross_origin
import uuid
from app import app
from flask import request
import database


@app.route('/signup/', methods=['POST', 'OPTIONS'])
@cross_origin()
def signup():
    userId = request.json.get('email')
    if '@' not in userId:
        return {'message': 'Email is invalid'}
    password = request.json.get('password')
    if not password:
        return {'message': 'Enter Password'}
    firstname = request.json.get('firstName')
    if not firstname:
        return {'message': 'Enter First Name'}
    lastname = str(request.json.get('lastName'))
    if not lastname:
        return {'message': 'Enter Last Name'}
    family_role = request.json.get('familyRole')
    paybox_id = str(request.json.get('paybox_id'))
    family_id = uuid.uuid4()
    if request.json.get('family_id'):
        family_id = request.json.get('family_id')
    database.users_table.UsersTable().insert_user(email=userId, password=password, family_id=family_id,
                                                  family_role=family_role,
                                                  firstname=firstname, lastname=lastname, paybox_id=paybox_id)

    return {'message': 'signup successfully', 'family_id': family_id}


@app.route('/user/<string:user_id>', methods=['PUT', 'OPTIONS'])
@cross_origin()
def modify_user(user_id: str):
    password = request.json.get('password')
    firstname = request.json.get('firstName')
    lastname = request.json.get('lastName')
    database.users_table.UsersTable().update_user(email=user_id, password=password, firstname=firstname,
                                                  lastname=lastname)

    return {'message': 'updated successfully'}


@app.route('/user/<string:user_id>', methods=['DELETE', 'OPTIONS'])
@cross_origin()
def delete_user(user_id: str):
    database.users_table.UsersTable().delete_user(email=user_id)
    database.user_amount_table.UsersAmountTable().delete_user(user_id)
    database.user_actions_table.UsersActionTable().delete_user(user_id)
    database.user_target_table.UsersTargetsTable().delete_user(user_id)

    return {'message': 'deleted successfully'}
