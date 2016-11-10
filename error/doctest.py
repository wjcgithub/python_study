#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'

def c_abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> c_abs(1)
    1
    >>> c_abs(-1)
    1
    >>> c_abs(0)
    0
    '''
    return n if n >= 0 else (-n)

print(c_abs(-19))