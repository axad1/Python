import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

sql = '''CREATE TABLE IF NOT EXISTS Customer(
	id INTEGER,
	name TEXT
)'''

# Execute
cur.execute(sql)

# Commit
conn.commit()

conn.close()