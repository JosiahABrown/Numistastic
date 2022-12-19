import sqlite3

DB = './db/coins.db'


class Database:
    def __init__(self, database_name):
        if not isinstance(database_name, str):
            raise TypeError('database_name must be a string')
        self.conn = sqlite3.connect(database_name)
        self.c = self.conn.cursor()

        # Enable foriegn key support
        self.conn.execute("PRAGMA foriegn_keys = ON")

    def execute_sql_file(self, file_path):
        # Read file
        with open(file_path, 'r') as f:
            sqlfile = f.read()

        # Split variable by ;
        sqlcommands = sqlfile.split(';')

        # Execute sql
        for command in sqlcommands:
            try:
                self.c.execute(command)
            except sqlite3.OperationalError:
                print("OperationalError. Command Skipped")

        # Commit commands
        self.conn.commit()

    def close(self):
        self.conn.close()


def main():
    db = Database(DB)
    db.execute_sql_file('sql_files/coins_table.sql')
    db.close()


main()
