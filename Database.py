import sqlite3


class Database:

    def __init__(self, db):
        self.con = sqlite3.connect(db)

        self.cur = self.con.cursor()

        self.con.commit()


db = Database("Employee.db")