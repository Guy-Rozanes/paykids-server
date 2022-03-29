from . import connection


class UsersTable():
    def insert_user(self, email, firstname, lastname, family_role, paybox_id):
        try:
            connection.connection.execute(f'INSERT INTO COMPANY (UserId,firstname,lastname,family_role,paybox_id) \
        VALUES ({email}, {firstname}, {lastname}, {family_role}, {paybox_id} )')
        except:
            raise Exception('Can not sign up')

    def get_user_by_email(self, email):
        return connection.connection.execute(f'SELECT FROM USERS WHERE UserId={email}')

    def update_paybox_id(self, email, paybox_id):
        return connection.connection.execute(f'UPDATE USERS SET paybox_id={paybox_id} WHERE UserId={email}')
