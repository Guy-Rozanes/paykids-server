import requests


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
        url = 'https://paybox.com.co/bills'
        headers = {
            'AUTHORIZATION': f'Bearer token{self.group_id}'
        }
        payload = {
            'groupId': self.group_id,
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text
