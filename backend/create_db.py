import sqlite3
import csv

DB = './db/coins.db'

def convert(list):
    return tuple(list)

class Database:
    def __init__(self, database_name):
        if not isinstance(database_name, str):
            raise TypeError('database_name must be a string')
        self.conn = sqlite3.connect(database_name)
        self.c = self.conn.cursor()

        # Enable foriegn key support
        self.conn.execute("PRAGMA foriegn_keys = ON")
        self.conn.commit()

    def execute_sql_file(self, file_path):
        # Read file
        with open(file_path, 'r') as f:
            sqlfile = f.read()

        self.c.executescript(sqlfile)

        # Commit commands
        self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    db = Database(DB)
    # db.execute_sql_file('sql_files/coins_table.sql')
    db.execute_sql_file('sql_files/us_coin_details.sql')
    db.close()