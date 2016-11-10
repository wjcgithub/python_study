#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
    finally:
        print('finally...')

main()
print('END')


# 自定义错误,并抛出
class FooError(ValueError):
    pass

def foo(s):
    n=int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10/n

foo(5)
foo(0)