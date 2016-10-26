#!/usr/bin/env python3
# -*- coding:utf-8 -*-
names = ['zhangsan', 'lisi', 'wangwu']
for name in names:
    print(name)

sum=0
for num in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+num
print(sum)

print(list(range(10)))
sum=0
for num in list(range(101)):
    sum=sum+num
print(sum)

#计算100以内所有奇数之和
sum=0
n=99
while n>0:
    sum = sum+n
    n = n-2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello,',name ,'!')