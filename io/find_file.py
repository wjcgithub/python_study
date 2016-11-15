#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
import os,os.path
os.environ.update()
# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def findFile(dir, findname):
    if os.path.isdir(dir):
        for x in os.listdir(dir):
            if(x=='.' or x=='..'):
                continue
            newdirorfile = os.path.join(dir,x)
            if os.path.isdir(newdirorfile):
                findFile(newdirorfile,findname)
            else:
                filename=os.path.split(newdirorfile)
                _index=filename[1].find(findname)
                if(_index>=0):
                    print(newdirorfile)
    else:
        print(dir+'不是一个路径')

if __name__=='__main__':
    findFile('/www/store/','demo')