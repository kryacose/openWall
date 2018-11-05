import sqlite3

class DB:

    def __init__(self, db_loc):
        self.db_loc = db_loc


    def execute(self, query):
        conn = sqlite3.connect(self.db_loc)
        c = conn.cursor()
        try:
            r=c.execute(query)
        except Exception as e:
            return e
        else:
            res = r.fetchall()
            conn.commit()
            conn.close()
            return res
        


    def fullRefresh(self):
        self.execute("drop table if exists users")
        self.execute("drop table if exists posts")

        self.execute("create table users( username varchar(25) primary, password varchar(25), dob date)")
        self.execute("create table posts( postid int, username varchar(25), )")
        