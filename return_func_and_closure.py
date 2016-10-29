#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# return function
def calc_sum(*args):
    sums=0
    for n in args:
        sums = sums+n
    return sums

print(calc_sum(1,3,5,7,9))

def lazy_sum(*args):
    def c_sum():
        sums=0
        for n in args:
            sums=sums+n
        return sums
    return c_sum

f=lazy_sum(1,3,5,7,9)
print(f())

#closure
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3=count()
print(f1())
print(f2())
print(f3())

# 你可能认为调用f1()，f2()和f3()结果应该是1，4，9
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def count():
    def f(j):
        def p():
            return j*j
        return p
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3=count()
print(f1())
print(f2())
print(f3())