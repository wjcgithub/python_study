#!/usr/bin/env python3
# -*- coding:utf-8 -*-
g=(x*x for x in range(10))
print(g)
for n in g:
    print(n)


def fib(max):
    n,a,b=0,0,1
    while n < max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'

fib(6)

def fib1(max):
    n,a,b=0,0,1
    while n < max:
        yield b
        a,b=b,a+b
        n=n+1
    return

print('=============')

for n in fib1(6):
    print(n)
