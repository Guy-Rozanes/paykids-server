import sqlite3
import uuid


class UsersActionTable():
    def get_action_by_userId(self, email):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'SELECT * FROM UsersActions WHERE UserId="{email}"')
            return cur.fetchall()

    def add_user_actions(self, user_id, action_name, action_price):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'INSERT INTO UsersActions (ActionId,UserId,ActionName,ActionPrice,Seen) VALUES ( "{uuid.uuid4()}", "{user_id}","{action_name}","{action_price}",{False})')
            conn.commit()

    def get_all_family_actions(self, family_id):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'SELECT UsersActions.UserId,UsersActions.ActionId,UsersActions.ActionName,UsersActions.ActionPrice,UsersActions.Seen FROM UsersActions JOIN Users ON Users.UserId=UsersActions.UserId where Users.FamilyId="{family_id}"')
            return cur.fetchall()


    def update_seen_to_true(self,action_id):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'Update UsersActions SET Seen={True} Where ActionId="{action_id}"')
            conn.commit()
