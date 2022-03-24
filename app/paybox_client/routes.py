from app import app
from flask import request


@app.route('/create', methods=['POST'])
def create():
    return "Hello world"


@app.route('/account/<int:account_id>')
def get_account_bill(account_id: int):
    return {'message': data[account_id]}


@app.route('/account/<int:account_id>', methods=['DELETE'])
def delete_account_bill(account_id: int):
    data.pop(account_id)
    return {'message': f'{account_id} bill has been deleted'}


@app.route('/account/<int:account_id>', methods=['PUT'])
def make_a_withdrawl(account_id: int):
    money = int(request.args.get('money'))
    data[account_id]['amount_money'] = int(data[account_id]['amount_money']) - money
    return {'message': f'withdrawl {money} accepted'}


data = {
    1: {
        'name': 'guy rozanes',
        'paybox_account_id': '183183123',
        'amount_money': '200',
    },
    2: {
        'name': 'guy rozanes',
        'paybox_account_id': '183183123',
        'amount_money': '200',
    },
    3: {
        'name': 'guy rozanes',
        'paybox_account_id': '183183123',
        'amount_money': '200',
    }
}
