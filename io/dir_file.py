#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
import os
import os.path

print(os.name)
# 获取机器名称
print(os.uname())
# 获取全部环境变量
print(os.environ)
# 获取指定的环境变量,并提供默认值
print(os.environ.get('PATH', 'default'))

#　获取某个路径的决定路径
print(os.path.abspath('.'))
# 目录链接　　把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
print(os.path.join('/home/evolution/PycharmProjects/example/io', 'testdir'))
# 通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('/home/evolution/PycharmProjects/example/io/testdir'))
# 获取文件名称的扩展
print(os.path.splitext('a/b/c/d.html.php'))
# 创建目录
os.mkdir('/home/evolution/PycharmProjects/example/io/testdir')
# 删除目录
os.rmdir('/home/evolution/PycharmProjects/example/io/testdir')

# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
# os.path.join()
# os.path.split()
# os.path.splitext()

x='../../'
[x for x in os.listdir('.') if os.path.isdir(x)]
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']