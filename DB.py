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
            conn.close()
            return e
        else:
            res = r.fetchall()
            conn.commit()
            conn.close()
            return res
        


    def Refresh(self):
        self.execute("drop table if exists users")
        self.execute("drop table if exists posts")

        self.execute('''create table users(
                        username varchar(50) PRIMARY KEY,
                        pw varchar(50),
                        fname varchar(100),
                        lname varchar(100),
                        dob date,
                        sex varchar(20),
                        aboutme varchar(200)
                    );''')


        self.execute('''create table posts(
                        postid int PRIMARY KEY,
                        username varchar(50),
                        timestmp timestamp,
                        likes int,
                        postdescpt varchar(200)
                    );''')
        

    #add post
    def addPost(self, username, desc):
        postid = self.execute('select count(*) from posts;')[0][0]
        q = f"insert into posts values( {postid}, '{username}', datetime('now','localtime'), 0 ,'{desc}');"

        print(q)
        return self.execute(q)

    def likePost(self, postid):
        q=  f"UPDATE posts SET likes = likes + 1 WHERE postid = {postid};"
        print(q)
        return self.execute(q)


    #add users
    def addUser(self, username, password, fname, lname, date, sex, desc):
        q = f"insert into users values('{username}', '{password}', '{fname}', '{lname}', '{date}', '{sex}', '{desc}');"
        return self.execute(q)


    #list users
    def listUser(self):
        q = "select username, fname, lname, dob, sex, aboutme from users;"
        return self.execute(q)


    #get User data
    def getUserInfo(self, username):
        q = f"select username, fname, lname, dob, sex, aboutme from users where username = '{username}';"
        return self.execute(q)


    #list posts
    def listAllPost(self):
        q = "select * from posts order by timestmp;"
        return self.execute(q)

    #list user posts
    def listUserPost(self, username):
        q = f"select * from posts where username ='{username}' order by timestmp;"
        print(q)
        return self.execute(q)

    #verify user
    def login(self, username, password):
        q = f"select pw from users where username = '{username}';"
        r = self.execute(q)
        # print(r,[(password,)])
        if(r == [(password,)]):
            return 1
        return 0