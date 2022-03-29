from app import app
from flask import request
from database import users_table


@app.route('/signup', methods=['POST'])
def signup():
    userId = request.args.get('email')
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')
    family_role = request.args.get('familyRole')
    paybox_id = request.args.get('paybox_id')
    try:
        users_table.UsersTable().insert_user(userId, firstname, lastname, family_role, paybox_id)
    except:
        pass
    return True
