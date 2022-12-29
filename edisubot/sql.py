import sqlite3


class SQL():

    def __init__(self, nome_db):
        self.nome_db = nome_db

    def conn(self):
        if not self.con: self.con = sqlite3.connect(self.nome_db)
    
    def close(self):
        if self.con: self.con.close()
    
    def execute(self, command, commit = False, fetch = False):

        self.conn()
        cur = self.con.cursor()
        res = cur.execute(command)
        if commit:
            self.con.commit()

        cur.close()
        self.close()

        if fetch: return res.fetchall()


