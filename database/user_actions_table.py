from . import connection


class UsersActionTable():
    def insert_user_action(self, email, action_name, action_payment):
        try:
            connection.connection.execute(f'INSERT INTO USERSACTIONS (UserId,ActionName,ActionPayment) \
        VALUES ({email}, {action_name}, {action_payment})')
        except:
            raise Exception('Can not insert this action')

    def delete_action(self, action_id):
        return connection.connection.execute(f'DELETE FROM USERSACTIONS where ACTIONID={action_id}')
