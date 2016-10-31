#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# from functools import reduce

# map
L = list(map(str,[1,2,3,4,5,6,7,8,9]))
print(L)

# reduce1
def add(x,y):
    return x+y
# print(reduce(add,[1,2,3,4,5,6]))

# reduce2
def fn(x,y):
    return x*10+y
# reduce(fn,[1,3,5,7,9])

#reduce3
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# reduce(fn,map(char2num, '13579'))