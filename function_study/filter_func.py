#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def not_empty(s):
    return s and s.strip()

L=list(filter(not_empty,['a','d','',None]))
print(L)


# 过滤回数
def is_palindrome(s):
    return str(s) == str(s)[::-1]

output=filter(is_palindrome,range(1,1000))
print(list(output))