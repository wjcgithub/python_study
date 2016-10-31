#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def fact(n):
    if n==1:
        return n
    return n * fact(n-1)

print(fact(5))