import requests
import random


class PayboxConnection():
    def __init__(self, username, password, group_id):
        self.username = username
        self.password = password
        self.group_id = group_id

    def create_a_payment(self, amount):
        result = requests.post(
            url='https://paybox.com.co/pay',
            headers={
                'AUTHORIZATION': 'Bearer test',
            },
            json={
                'order_id': 123456,
                'currency': 'NIS',
                'amount': amount,
                'mode': 'test',
                'mobile_network': 'AirtelTigo',
                'mobile_number': +972547747038,
                'card_first_name': self.username,
                'card_last_name': self.username,
                'card_number': 1111111111111111,
                'card_expiry': '2030-12'
            }
        )

        return result

    def get_group_bills(self, ):
        product_number = random.randint(0, 13)
        products = [
            {'product_name': 'Gum', 'product_price': 2},
            {'product_name': 'Magnoom', 'product_price': 10},
            {},
            {'product_name': 'Candy', 'product_price': 5},
            {'product_name': 'Supergoal', 'product_price': 15},
            {},
            {'product_name': 'T-Shirt', 'product_price': 30},
            {},
            {'product_name': 'Shoes', 'product_price': 200},
            {},
            {'product_name': 'Coca Cola', 'product_price': 9},
            {'product_name': 'Sprite', 'product_price': 8},
            {},
            {'product_name': 'Fuze Tea', 'product_price': 7},
        ]
        url = 'https://paybox.com.co/bills'
        headers = {
            'AUTHORIZATION': f'Bearer token{self.group_id}'
        }
        payload = {
            'groupId': self.group_id,
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return {
            'message': products[product_number]
        }

