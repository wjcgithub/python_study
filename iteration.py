#!/usr/bin/env python3
# -*- coding:utf-8 -*-

d={'a':1,'b':2,'c':3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k,v in d.items():
    print(k,v)

# 字符串迭代
for ch in 'ABCDE':
    print(ch)

for x,y,z in [(1,1,1),(2,4,6),(3,6,9)]:
    print(x, y, z)

# test
# print(isinstance('abc',Iterable))
# print(isinstance([1,2,3],Iterable))
# print(isinstance(123,Iterable))
# print(isinstance((1,2,3),Iterable))
# print(isinstance({'a':1,'b':2},Iterable))