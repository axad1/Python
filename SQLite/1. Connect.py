import sqlite3

# Connection
conn = sqlite3.connect('data.db')
# conn = sqlite3.connect(':memory:')

# Cursor
cur = conn.cursor()

# Close
conn.close()