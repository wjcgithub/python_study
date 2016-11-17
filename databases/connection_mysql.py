#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
import mysql.connector

# 连接数据库
conn=mysql.connector.connect(user='root', password='brave', database='test')

# 创建
# cursor=conn.cursor()
# cursor.execute('create table python_ct (id int PRIMARY KEY , name VARCHAR(20))')

# 插入
# cursor.execute('insert into python_ct (id, name) VALUES (%s, %s)', [1, 'wjc'])
# cursor.rowcount
# conn.commit()
# cursor.close()

# 查询
cursor=conn.cursor()
cursor.execute('select * from python_ct')
values=cursor.fetchall()
print(values)
print(values[0][0])
print(values[0][1])

# 关闭
cursor.close()
conn.close()