import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()


sql = "INSERT INTO Customer VALUES(1, 'John')"
# Execute single command
cur.execute(sql)


sql = [
	(2, 'Ben'),
	(3, 'Hanna')
]
# Execute multiple commands
cur.executemany("INSERT INTO Customer VALUES(?,?)", sql)


# important point
# sql = ['ali','hamza']
# cur.executemany("INSERT INTO student(name) VALUES(?)", [(i,) for i in sql])

conn.commit()
conn.close()