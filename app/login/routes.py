from flask_cors import cross_origin

from app import app
from flask import request, Response, jsonify
from database import users_table


@app.route("/login/", methods=['POST', 'OPTIONS'])
@cross_origin()
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    user = users_table.UsersTable().get_user_by_email(email)
    if not user:
        return {'message': 'login failed'}
    if user[6] == password:
        return {'message': 'login successfully', 'user': user}
    else:
        return {'message': 'login failed'}
