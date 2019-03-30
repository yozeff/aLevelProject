#Joseph Harrison 2019
#A Level Project
#Module 8: Storing Datasets
import sqlite3 as sql

class Session:

    #create our session connection
    #and cursor instances
    def __init__(self,dbname):
        self.conn = sql.connect(dbname)
        self.cursor = self.conn.cursor()

    #close our connection
    def close(self):
        self.conn.close()

sesh = Session(':memory:')
sesh.close()
