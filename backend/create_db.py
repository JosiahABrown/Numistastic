import sqlite3

DB = './db/coins.db'


def create_tables():
    conn = sqlite3.connect(DB)
    print(f"=== Connected to the {DB[-8:-3]} Database ===")
    c = conn.cursor()

    print("Reading SQL")
    with open('sql_files/coins_table.sql', 'r') as fd:
        sqlfile = fd.read()

    sqlcommands = sqlfile.split(';')

    print("Executing SQL")
    for command in sqlcommands:
        try:
            c.execute(command)
        except sqlite3.OperationalError:
            print("Operational Error. Commmand skipped.")

    conn.commit()
    conn.close()
    print("=== Connection Closed ===")


create_tables()
