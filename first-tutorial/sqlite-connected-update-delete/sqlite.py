import sqlite3

class SqliteHelper:
    def __init__(self, name=None):
        self.conn = None
        self.cursor = None
        
        if name:
            self.open(name)
    def open(self,name):
        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()
            print(sqlite3.version)
        except sqllite.Error as e:
            print("Failed connecting to the database!")
    def create_table(self):
        c = self.cursor
        c.execute("""
            CREATE TABLE user(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   year INTEGER,
                   admin INTEGER
            )          
                  
        """)        

    def edit(self, query, updates):  #update
        c = self.cursor
        c.execute(query, updates)
        self.conn.commit()
        
    def insert(self, query, inserts):  #insert
        c = self.cursor
        c.execute(query, inserts)
        self.conn.commit()      
    def delete(self, query):  #delete
        c = self.cursor
        c.execute(query)
        self.conn.commit()
        
    def select(self, query):   #select
        c = self.cursor
        c.execute(query)
        return c.fetchall()
        

#test = SqliteHelper("test.db")  
#test.create_table()    
#test.edit("INSERT INTO user (name, year, admin) VALUES ('John',1992,0)")
#print(test.select("SELECT * from user"))
#test.edit("UPDATE user SET name='Jack' WHERE name='John'")  
#print(test.select("SELECT * from user"))         