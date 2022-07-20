import sqlite3

import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'paykids.db')


class UsersCardTable():
    def insert_card(self, email,last4_numbers,exp_card):
        with sqlite3.connect(filename, isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'INSERT INTO CardExp (UserId,CardLast4,CardExp) VALUES ("{email}", "{last4_numbers}","{exp_card}")')
            conn.commit()

    def delete_card(self,last4_numbers,exp_card):
        with sqlite3.connect(filename, isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'Delete from CardExp where CardLast4="{last4_numbers}" and CardExp="{exp_card}"')
            conn.commit()

    def get_card_by_email(self, email):
        with sqlite3.connect(filename, isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'Select * from CardExp where UserId="{email}"')
            return cur.fetchall()