#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
# return None可以简写为return

def my_abs(num):
    if num>0:
        return num
    elif num<0:
        return -num


print(my_abs(-5))


# 空函数
##如果想定义一个什么事也不做的空函数，可以用pass语句：
##pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass

nop()


# 给函数添加类型检测
def my_abs(num):
    if not isinstance(num, (int, float)):
        raise TypeError('bad operand type')
    if num>0:
        return num
    elif num<0:
        return -num

print(my_abs(-5))
print(my_abs('123'))