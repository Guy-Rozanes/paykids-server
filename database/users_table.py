import sqlite3

import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'paykids.db')


class UsersTable():
    def update_user(self, email, password, firstname, lastname):
        with sqlite3.connect(filename, isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'Update Users SET FirstName="{firstname}" ,LastName="{lastname}",Password="{password}" where UserId="{email}"')
            conn.commit()

    def delete_user(self, email):
        with sqlite3.connect(filename, isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'DELETE from Users where UserId="{email}"')
            conn.commit()

    def insert_user(self, email, password, family_id, family_role, firstname, lastname, paybox_id):
        with sqlite3.connect(filename, isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'INSERT INTO Users (UserId,FamilyId,FamilyRole,FirstName,LastName,PayboxId,Password) VALUES ( "{email}", "{family_id}","{family_role}","{firstname}","{lastname}","{paybox_id}","{password}" )')
            conn.commit()

    def get_user_by_email(self, email):
        with sqlite3.connect(filename, isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'SELECT Users.UserId,Users.FamilyId,Users.FamilyRole,Users.FirstName,Users.LastName,Users.PayboxId,Users.Password,FamilyAccountType.AccountType FROM Users JOIN FamilyAccountType ON Users.FamilyId=FamilyAccountType.FamilyId where Users.UserId="{email}"')
            rows = cur.fetchall()
        if len(rows) > 0:
            return rows[0]
        else:
            return None

    def get_my_family(self, family_id):
        with sqlite3.connect(filename, isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(f'Select * from Users where FamilyId="{family_id}"')
            return cur.fetchall()

    def get_my_kids(self, family_id):
        with sqlite3.connect(filename, isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(f'Select * from users where users.FamilyRole!="Owner" and users.FamilyId="{family_id}"')
            return cur.fetchall()
