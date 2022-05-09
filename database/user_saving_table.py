import sqlite3
import uuid


class UserSavingsTable():
    def add_saving_exc(self, email,video_name,saving_price):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'INSERT INTO UserSavings (UserId,SavingId,SavingName,SavingPrice,Status)VALUES ("{email}","{uuid.uuid4()}","{video_name}","{saving_price}",{False})')
            conn.commit()

    def get_my_saving(self, email):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'SELECT * from UserSavings where UserId="{email}"')
            return cur.fetchall()

    def update_status(self, saving_id):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'UPDATE UserSavings set Status=1 where SavingId="{saving_id}"')
            conn.commit()
