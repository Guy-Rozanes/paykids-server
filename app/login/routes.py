from app import app
from flask import request


@app.route("/login")
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    for item in users:
        if item['username'] == username:
            if item['password'] == password:
                return {'message': 'login successfully'}

    return {'message':'login failed user or password is incorrect'}



users = [
    {
        'username': 'guy rozanes',
        'password': '123',
    },
    {
        'username': 'bla bla',
        'password': '123',
    }
]
