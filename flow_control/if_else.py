#!/usr/bin/env python
# -*- coding:utf-8 -*-

# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

age = 32
if age>=18:
    print("adult")
elif age>=6:
    print('teenager')
else:
    print('kid')


# 接收用户的输入来判断，注意字符串和整数的转换
age = input("请输入您的年龄：")
age = int(age)   # 需要转换一下
if age>=18:
    print("adult")
elif age>=6:
    print('teenager')
else:
    print('kid')


while True:
    height = float(input('请输入身高m：'))
    weight = float(input('请输入体重kg：'))
    bmi = weight/(height*height)
    print(bmi)
    if bmi<=18.5:
        print("体重过轻")
    elif bmi>=18.5 and bmi<=25:
        print('正常')
    elif bmi>=25 and bmi <= 28:
        print('过重')
    elif bmi >= 28 and bmi <= 32:
        print('肥胖')
    elif bmi>=32:
        print('严重肥胖')
