from flask_cors import cross_origin

from app import app
from flask import request, Response, jsonify
from database import family_type_table


@app.route("/family/account", methods=['POST', 'OPTIONS'])
@cross_origin()
def add_family_account_type():
    family_id = request.json.get('familyId')
    account_type = request.json.get('accountType')
    family_type_table.FamilyTypeTable().add_family_account_type(family_id, account_type)
    return {'message': 'ok'}


@app.route("/family/premium/<string:family_id>", methods=['PUT'])
@cross_origin()
def update_account_type(family_id):
    account_type = request.json.get('accountType')
    family_type_table.FamilyTypeTable().update_family_account_type(family_id, account_type)
    return {'message': 'ok'}
