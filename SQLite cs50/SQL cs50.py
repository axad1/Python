import cs50

# db must exist to before connect
db = cs50.SQL("sqlite:///test.db")

# create table
db.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER, name TEXT)")

# insert
db.execute("INSERT INTO test VALUES(1, 'asad')")

# select returns a list of dictionaries
rows = db.execute("SELECT * FROM test")

print(rows)


'''
db = cs50.SQL("sqlite:///file.db")  # For SQLite, file.db must exist
db = cs50.SQL("mysql://username:password@host:port/database")  # For MySQL
db = cs50.SQL("postgres://username:password@host:port/database")  # For PostgreSQL
'''