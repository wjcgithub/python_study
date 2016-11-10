#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
from enum import Enum,unique

Month=Enum('age',('a','b','c'))

# print(Month)

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Mon.value)