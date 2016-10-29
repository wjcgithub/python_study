#!/usr/bin/env python3
# -*- coding:utf-8 -*-
L=sorted([23,67,1,9,-43,-2])
print(L)

L=sorted([23,67,1,9,-43,-2],key=abs)
print(L)

L=sorted(['abd','Ed','DD','uifG','Epw'],key=str.lower)
print(L)

L=sorted(['abd','Ed','DD','uifG','Epw'],key=str.lower,reverse=True)
print(L)

# 将以下列表按照学生姓名进行排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()

def by_score(t):
    return t[1]

L2 = sorted(L,key=by_name)
L3 = sorted(L,key=by_score)
print(L2)
print(L3)



