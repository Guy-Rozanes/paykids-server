from flask_cors import cross_origin
from flask import request
from app import app
from database import user_saving_table


@app.route("/savings/", methods=['POST', 'OPTIONS'])
@cross_origin()
def add_saving():
    user_id = request.json.get('email')
    video_name = request.json.get('videoName')
    savings_price = request.json.get('savingPrice')
    try:
        user_saving_table.UserSavingsTable().add_saving_exc(user_id, video_name, savings_price)
        return {'message': 'Inserted successfully'}
    except:
        return {'message': 'error'}


@app.route("/savings/<string:user_id>", methods=['GET', 'OPTIONS'])
@cross_origin()
def get_my_saving(user_id):
    try:
        my_savings = user_saving_table.UserSavingsTable().get_my_saving(user_id)
        return {'message': my_savings}
    except:
        return {'message': 'error'}
