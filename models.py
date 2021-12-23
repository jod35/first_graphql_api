from sqlalchemy import (
    create_engine,
    Column,
    String,
    Integer,
    Text,
    ForeignKey,
    )
from sqlalchemy.orm import backref, declarative_base,relationship,sessionmaker
import os

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

conn_string='sqlite:///'+os.path.join(BASE_DIR,'site.db')

engine=create_engine(conn_string,echo=True)

Base=declarative_base()

class User(Base):
    __tablename__='users'
    id=Column(Integer(),primary_key=True)
    first_name=Column(String(40),nullable=False)
    last_name=Column(String(40),nullable=True)
    email=Column(String(80),nullable=False)
    posts=relationship('Post',backref='author')


    def __rep__(self):
        return f"<User {self.first_name}"



class Post(Base):
    __tablename__='posts'
    id=Column(Integer(),primary_key=True)
    title=Column(String(40),nullable=False)
    content=Column(Text(),nullable=False)
    user=Column(Integer(),ForeignKey('users.id'))


    def __repr__(self):
        return f"<User {self.title}>"


