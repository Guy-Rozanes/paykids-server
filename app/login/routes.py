from app import app
from flask import request, Response
from database import users_table


@app.route("/login")
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    user = users_table.UsersTable().get_user_by_email(email)
    if user[0]['password'] == password:
        return Response({'message': 'login successfully'}, 200)
    else:
        return Response({'message': 'login failed'}, 406)
