from flask_cors import cross_origin
import uuid
from app import app
from flask import request
from database import users_table


@app.route('/signup/', methods=['POST', 'OPTIONS'])
@cross_origin()
def signup():
    userId = request.json.get('email')
    password = request.json.get('password')
    firstname = request.json.get('firstName')
    lastname = str(request.json.get('lastName'))
    family_role = request.json.get('familyRole')
    paybox_id = str(request.json.get('paybox_id'))
    family_id = uuid.uuid4()
    if request.json.get('family_id'):
        family_id = request.json.get('family_id')
    users_table.UsersTable().insert_user(email=userId, password=password, family_id=family_id, family_role=family_role,
                                         firstname=firstname, lastname=lastname, paybox_id=paybox_id)

    return {'message': 'signup successfully'}


