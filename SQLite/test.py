import sqlite3

db = sqlite3.connect('test.db')
cur = db.cursor()

sql = "SELECT * FROM test"


cur.execute(sql)

data = cur.fetchall()

for i in data:
	print(i[0])


db.commit()
db.close()