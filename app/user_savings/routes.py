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


@app.route("/savings/family/<string:family_id>", methods=['GET', 'OPTIONS'])
@cross_origin()
def get_family_saving(family_id):
    result = {}
    my_savings = user_saving_table.UserSavingsTable().get_all_family_savings(family_id)
    for user_saving in my_savings:
        if result.get(user_saving[0]):
            result[user_saving[0]].append(
                {
                    'user_id': user_saving[0],
                    'saving_id': user_saving[1],
                    'saving_name': user_saving[2],
                    'saving_price': user_saving[3],
                    'status': user_saving[4],
                }
            )
        else:
            result[user_saving[0]] = []
            result[user_saving[0]] = [
                {
                    'user_id': user_saving[0],
                    'saving_id': user_saving[1],
                    'saving_name': user_saving[2],
                    'saving_price': user_saving[3],
                    'status': user_saving[4],
                }
            ]
    return {'message': result}


@app.route("/savings/<string:saving_id>", methods=['PUT', 'OPTIONS'])
@cross_origin()
def mark_task_as_complete(saving_id):
    try:
        user_saving_table.UserSavingsTable().update_status(saving_id)
        return {'message': 'Task mark has completed'}
    except:
        return {'message': 'error'}
