#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'

L=[1,2,3,4,5]
print(type(L))
print(type(L[:]))
print(L)
print(L[:])
# exit()

def triangles():
    L = [1]
    while True:
        yield L
        L1 = [0] + L[:]
        L = [L[i]+L1[i] for i in range(len(L))] + [1]

n=0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break