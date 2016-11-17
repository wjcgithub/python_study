#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker,relationships
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base=declarative_base()

# 定义user对象
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationships('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))
engine=create_engine('mysql+mysqlconnector://root:brave@localhost:3306/test')
DBSession=sessionmaker(bind=engine)

# 查询数据
session=DBSession()
user=session.query(User).filter(User.id==2).one()
print('type:', type(user))
print('name:', user.name)
session.close()