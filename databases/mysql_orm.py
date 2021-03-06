#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base=declarative_base()

# 定义user对象
class User(Base):
    __tablename__='python_ct'

    #表结构
    id=Column(String(20), primary_key=True)
    name=Column(String(20))

engine=create_engine('mysql+mysqlconnector://root:brave@localhost:3306/test')
DBSession=sessionmaker(bind=engine)

# 使用对象方式向数据库中添加数据
# session=DBSession()
# userObj = User(id=2, name='zs')
# session.add(userObj)
# session.commit()
# session.close()

# 查询数据
session=DBSession()
user=session.query(User).filter(User.id==2).one()
print('type:', type(user))
print('name:', user.name)
session.close()