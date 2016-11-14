#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'

#read 字符串文件
f=open('./input.py','r')
print(f.read())
f.close()

# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
try:
    f=open('./input.py','r')
    print(f.read())
finally:
    if f:
        f.close()


# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
with open('input.py','r') as f:
    print(f.close())


with open('input.py','r') as f:
    l=f.readlines()
    for line in l:
        print(line.strip())

    str=f.readline()
    print(str)


# 读取二进制文件
with open('../images/car.jpg','rb') as f:
    print(f.read())


# 读取指定字符集的文件
f=open('input.py','r',encoding='gbk')
print(f.read())

f=open('input.py','r',encoding='gbk',errors='ignore')
print(f.read())


#写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：