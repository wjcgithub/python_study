#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#list  有序可变列表
L=['a','b','c',['d','e',['f']]]
L.append('i')
L.pop(4)
L.insert(1,'Jack')
L[2] = 'wjc'
L[3][0]
len(L)
print(L)

#tuple  有序不可变列表
T=('a',)
T=(1,)
T=(1,2,3,4,5)
T=(1,2,3,4,[5,6,7])
#T[2] = '2'    # 不可以赋值
T[4][1] = 9   # 可以赋值tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
print(T)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])