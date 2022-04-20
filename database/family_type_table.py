import sqlite3
import uuid


class FamilyTypeTable():
    def add_family_account_type(self, family_id, account_type):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(
                f'INSERT INTO FamilyAccountType (FamilyId,AccountType) VALUES ( "{family_id}","{account_type}")')
            conn.commit()

    def update_family_account_type(self, family_id, account_type):
        with sqlite3.connect(r'C:\Users\Guy Rozanes\Desktop\paykids.db', isolation_level=None) as conn:
            cur = conn.cursor()
            cur.execute(f'UPDATE FamilyAccountType Set AccountType="{account_type}" WHERE FamilyId="{family_id}"')
            conn.commit()
    