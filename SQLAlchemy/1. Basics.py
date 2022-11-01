import sqlalchemy

print(sqlalchemy.__version__)

engine = sqlalchemy.create_engine("sqlite+pysqlite:///test.db", echo=True, future=True)
# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

conn = engine.connect()

conn.execute(sqlalchemy.text("CREATE TABLE IF NOT EXISTS test(id INTEGER, name TEXT)"))

# conn.execute(sqlalchemy.text("INSERT INTO test VALUES(1, 'Asad')"))

result = conn.execute(sqlalchemy.text("SELECT * FROM test"))

# print(result.one())
print(result.all())

conn.commit()

'''
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())
'''