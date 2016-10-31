#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'

from PIL import Image
import sys

im = Image.open('./images/car.jpg')
print(im.format, im.size, im.mode)

print(sys.path)

#如果我们要添加自己的搜索目录，有两种方法：
#一是直接修改sys.path，添加要搜索的目录：
#sys.path.append('/Users/michael/my_py_scripts')
#这种方法是在运行时修改，运行结束后失效。
#第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。