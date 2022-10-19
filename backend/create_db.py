import sqlite3


def create_coins_table():
    conn = sqlite3.connect("./db/coins.db")
    c = conn.cursor()
    with open('sql_files/coins_table.sql', 'r') as fd:
        sqlfile = fd.read()

    sqlcommands = sqlfile.split(';')

    for command in sqlcommands:
        try:
            c.execute(command)
        except sqlite3.OperationalError:
            print("Commmand skipped.")

    conn.commit()
    conn.close()


create_coins_table()
