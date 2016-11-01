#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'

class Animal(object):
    name="金毛"

    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running')

class Cat(Animal):
    def run(self):
        print('Cat is running')


cat=Cat()
dog=Dog()

print(type(cat))
print(type(dog))

print(isinstance(cat,Cat))
print(isinstance(cat,Animal))
print(isinstance(cat,Dog))


print(isinstance([1,2,3], (list,tuple)))
print(isinstance((1,2,3), (list,tuple)))

print(dir(dog))
print(dir('ABC'))


print(hasattr(dog,'name'))
print(getattr(dog,'name'))
setattr(dog,'name','比熊')
print(getattr(dog,'name'))
print(getattr(dog,'color', '黄色'))

returnrun = getattr(dog, 'run')
returnrun()