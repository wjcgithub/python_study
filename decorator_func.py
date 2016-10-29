#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 装饰器
def log(b,e):
    def decorator(func):
        def wrapper(*args,**kw):
            # print(func.__name__)
            print("%s cal" %(b))
            func(*args,**kw)
            print("%s cal" %(e))
        return wrapper
    return decorator

def start():
    print('processing...')

log=log('begin','end')
start = log(start)
start()