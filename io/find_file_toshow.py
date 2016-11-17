#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
import os,os.path,re,sys

# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def findFile(dir):
    if os.path.isdir(dir):
        for x in os.listdir(dir):
            if(x=='.' or x=='..'):
                continue
            newdirorfile = os.path.join(dir,x)
            if os.path.isdir(newdirorfile):
                findFile(newdirorfile)
            else:
                regex=r'^/.*app'
                newdirorfile, number = re.subn(regex, '', newdirorfile)
                print('/app'+newdirorfile)
    else:
        print(dir+'不是一个路径')

if __name__=='__main__':
    if(len(sys.argv)!=2):
        print('请输入一个路径信息')
    else:
        findFile(sys.argv[1])