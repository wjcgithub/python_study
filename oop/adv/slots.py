#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'

from types import MethodType

class Student(object):
    pass

s=Student()
s.name='lisi'
print(s.name)

def setAge(self, age):
    self.age=age

s.setAge=MethodType(setAge,s)
s.setAge(25)
print(s.age)

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score=10
print(s.score)


class Screen(object):
    resolution=111

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width=value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height=value

    @property
    def resolution(self):
        return self._resolution

s=Screen()
s.width=100
s.height=100
print(s.width)
print(s.height)
# s.resolution='fds'
print(s.resolution)