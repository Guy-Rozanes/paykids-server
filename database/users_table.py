from . import connection
import sqlite3


class UsersTable():
    def insert_user(self, email, password, family_id, family_role, firstname, lastname, paybox_id):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'INSERT INTO Users (UserId,FamilyId,FamilyRole,FirstName,LastName,PayboxId,Password) VALUES ( "{email}", "{family_id}","{family_role}","{firstname}","{lastname}","{paybox_id}","{password}" )')
            conn.commit()

    def get_user_by_email(self, email):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(f'Select * from Users where UserId="{email}"')
            rows = cur.fetchall()
        if len(rows) > 0:
            return rows[0]
        else:
            return None

    def update_paybox_id(self, email, paybox_id):
        return connection.connection.execute(f'UPDATE USERS SET paybox_id={paybox_id} WHERE UserId={email}')

    def get_my_family(self, family_id):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(f'Select * from Users where FamilyId="{family_id}"')
            return cur.fetchall()
