#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'

class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
        self.__eat='米饭'

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_eat(self):
        return self.__eat

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

zhangsan=Student('lisi', 93)
wjc=Student('wjc', 63)
zhangsan.print_score()
wjc.print_score()
print(zhangsan.get_grade())
print(wjc.get_grade())

wjc.eat='冰淇淋'
print(wjc.eat)
print(wjc.get_eat())