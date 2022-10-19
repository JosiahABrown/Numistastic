import sqlite3

conn = sqlite3.connect("./db/coins.db")

c = conn.cursor()

c.execute("""CREATE TABLE coins (
        denomination TEXT,
        nickname TEXT,
        country TEXT,
        mintage INT,
        metal TEXT
    )""")

conn.commit()
conn.close()
