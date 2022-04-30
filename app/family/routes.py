from flask_cors import cross_origin

from app import app
from flask import request, Response, jsonify
from database import users_table


@app.route("/family/<string:family_id>", methods=['GET'])
@cross_origin()
def get_family(family_id):
    users = users_table.UsersTable().get_my_family(family_id)
    if users:
        return {'message': users}
    else:
        return {'message': 'Please add members'}

@app.route("/kids/<string:family_id>", methods=['GET'])
@cross_origin()
def get_kids(family_id):
    users = users_table.UsersTable().get_my_kids(family_id)
    if users:
        return {'message': users}
    else:
        return {'message': 'Please add members'}