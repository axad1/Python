from sqlalchemy import create_engine, Column, String, Integer, DateTime, text, asc, desc
from datetime import datetime
from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite+pysqlite:///test.db", echo=False, future=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
localsession = Session()

# temporary line
engine.connect().execute(text("DROP TABLE IF EXISTS users"))

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
    email = Column(String(25), nullable=False, unique=True)
    date = Column(DateTime(), default=datetime.now)

    def __repr__(self):
        return f"{self.name} {self.email} {self.date}"

# create table
Base.metadata.create_all(engine)

# insert 1 data
localsession.add(User(name="Asad", email="abc@gmail.com"))

# insert 3 data
users = [
    {
        "name": "Ahsan",
        "email": "ahsan@email.com"
    },
    {
        "name": "Shaheen",
        "email": "shaheen@email.com"
    },
    {
        "name": "Hassan",
        "email": "hassan@email.com"
    },
]
for user in users:
    localsession.add(User(name=user["name"], email=user["email"]))

# insert list of all data
users = [User(name='Ali', email='ali@email.com'), User(name='Ahmad', email='ahmad@email.com')]
localsession.add_all(users)

# commit
localsession.commit()


# get
users = localsession.query(User)
# get a list of all
users = localsession.query(User).all()
# count
users = localsession.query(User).count()
# limit
users = localsession.query(User).all()[0:]
# order by ascending
users = localsession.query(User).order_by(User.name)
# order by descending
users = localsession.query(User).order_by(desc(User.name))
# filter
users = localsession.query(User).filter(User.name=="Asad")
# filter returns only one
user = localsession.query(User).filter(User.name=="Asad").first()


# update
user.name = "AxAd"
user.email = "asadhusn007@gmail.com"
localsession.commit()

# delete
user = localsession.query(User).filter(User.name=="Ahmad").first()
localsession.delete(user)
localsession.commit()
