#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1, 2))
print(calc())


nums = [1, 2, 3]
print(calc(*nums))


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('lisi',18)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extrac
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

# 命名关键字参数
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

# 命名关键字参数默认值
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('Jack', 24, job='Engineer')


#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数