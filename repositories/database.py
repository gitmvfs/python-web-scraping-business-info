import sqlite3

class Database():

    DEFAULT_FILE_PATH = str('repositories/database.db')

    def __init__(self, file_path:str = DEFAULT_FILE_PATH):
        self.connect(file_path)

    def connect(self, file_path:str = DEFAULT_FILE_PATH):

        self.database = sqlite3.connect(file_path)
        self.cursor = self.database.cursor() #implement actions in the database     

    def update(self):
        self.database.commit()
    
    def closeConnect(self):
        self.cursor.close()
        self.database.close()

    def execute_query(self, query:str, parameters=''):
        self.connect()
        self.cursor.execute(query, parameters)
        self.update()
        self.closeConnect()

    def execute_query_fetchall(self, query:str, parameters = () ) -> list:
        self.connect()
        self.cursor.execute(query, parameters)
        rows = self.cursor.fetchall()
        self.closeConnect()
        return rows