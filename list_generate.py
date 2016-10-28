#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

#e1
L = list(range(1,11))
print(L)

#e2
L=[]
for x in range(1,11):
    L.append(x*x)
print(L)

#e3
L=[x*x for x in range(1,11)]
print(L)

#e4
L=[x*x for x in range(1,11) if x%2 == 0]
print(L)

#e5
L=[x*x for x in range(1,11) if x%2 == 1]
print(L)

#e6
L=[m+n for m in 'ABC' for n in 'XYZ']
print(L)

#e7
L=[d for d in os.listdir('.')]
print(L)

#e8
d={'a':1, 'b':2, 'c':3}
# L=[k+str('=')+v for k,v in d.items()]
print(L)