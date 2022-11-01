import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

cur.execute("SELECT * FROM Customer")

# data = cur.fetchone()
# data = cur.fetchmany()
data = cur.fetchall()

for i in data:
    print(str(i[0]) + " | " + i[1])

conn.commit()
conn.close()