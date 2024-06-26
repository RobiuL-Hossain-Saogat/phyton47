import sqlite3

class Database:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS part (id INTEGER PRIMARY KEY, part text, customer text, price text, company text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM part ")
        rows=self.cur.fetchall()
        return rows
    
    def insert(self,part,customer,price,company):
        self.cur.execute("INSERT INTO part VALUES (NULL,?,?,?,?)",(part,customer,price,company))
        self.conn.commit()
