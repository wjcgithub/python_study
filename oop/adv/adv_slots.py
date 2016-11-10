#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'

class Student(object):
    __slots__=('name','age')  #用tuple定义允许绑定的属性名称

s=Student()
s.name='list'
s.age=19

print(s.name)
print(s.age)

# s.sex=1  #  这个将会报错，没有属性sex


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    pass

gs=GraduateStudent()
gs.score=900
print(gs.score)

# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class GStudent(Student):
    __slots__=('score')

gs=GStudent()
gs.name='zs'
gs.age=20
gs.score=90
# gs.addr='bj'   报告属性未定义
print(gs.name)
print(gs.age)
print(gs.score)