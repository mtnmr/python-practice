import sqlite3
import pandas as pd

df = pd.read_csv('パス名')

db_name = 'sample.db'
conn = sqlite3.connect(db_name)

df.to_sql('table name', conn, if_exists='replace')

c = conn.cursor()
query = 'SELECT * FROM table name'
c.execute(query)

c.fetchone()
c.fetchall()

for row in c.execute(query):
    print(row)

conn.close()


