import sqlite3
import uuid


class UsersTargetsTable():
    def get_target_by_email(self, email):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'SELECT * FROM UsersTargets WHERE UserId="{email}"')
            return cur.fetchall()

    def add_user_target(self, user_id, target_name, target_price):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'INSERT INTO UsersTargets (TargetId,UserId,TargetName,TargetPrice) VALUES ( "{uuid.uuid4()}", "{user_id}","{target_name}","{target_price}")')
            conn.commit()

    def get_all_family_targets(self, family_id):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'SELECT UsersTargets.UserId,UsersTargets.TargetId,UsersTargets.TargetName,UsersTargets.TargetPrice FROM UsersTargets JOIN Users ON Users.UserId=UsersTargets.UserId where Users.FamilyId="{family_id}"')
            return cur.fetchall()

    def delete_target(self, target_id):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(f'Delete from UsersTargets where TargetId="{target_id}"')
            conn.commit()

    def delete_user(self,user_id):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'Delete from UsersTargets WHERE UserId="{user_id}"')
            conn.commit()