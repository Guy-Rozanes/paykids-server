import sqlite3
import uuid


class UsersAmountTable():
    def get_user_amount(self, email):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'SELECT * FROM UserAmount WHERE UserId="{email}"')
            return cur.fetchall()

    def add_amount(self, user_id, bank_number, amount):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'INSERT INTO UserAmount (UserId,UserBankNumber,Amount) VALUES ( "{user_id}", "{bank_number}",{amount})')
            conn.commit()

    def update_amount(self, email, new_amount):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'UPDATE UserAmount SET Amount={new_amount} where UserId="{email}"')
            conn.commit()

    def get_all_family_amount(self, family_id):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'SELECT UserAmount.UserId,UserAmount.UserBankNumber,UserAmount.Amount FROM UserAmount JOIN Users ON Users.UserId=UserAmount.UserId where Users.FamilyId="{family_id}"')
            return cur.fetchall()

    def delete_user(self,user_id):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'Delete from UserAmount WHERE UserId="{user_id}"')
            conn.commit()