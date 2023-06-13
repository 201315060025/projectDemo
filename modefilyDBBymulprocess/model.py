# coding: utf-8
"""
关系映射模型
"""

from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql://root:123456@127.0.0.1/weixiang?charset=utf8")

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    email = Column(String(64))
    number = Column(Integer)

    def __init__(self, name, email):
        self.name = name
        self.email = email


Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

# 创建session
DbSession = sessionmaker(bind=engine)
session = DbSession()

# add_user = Users("test", "test123@qq.com")
# session.add(add_user)
# session.commit()


# record = session.query(Users).filter(Users.name == 'test').update({Users.number: Users.number + 1})
# print("---", record)
# session.commit()

