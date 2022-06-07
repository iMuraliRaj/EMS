import sqlite3


class Database:

    def __init__(self, db):
        self.con = sqlite3.connect(db)

        self.cur = self.con.cursor()

        sql = """

        CREATE TABLE IF NOT EXISTS employee

        (

        EMP ID Integer Primary Key,

        Name text,
        
        Department text,
        
        DOB text

        )


        """

        self.cur.execute(sql)

        self.con.commit()


db = Database("Employee.db")