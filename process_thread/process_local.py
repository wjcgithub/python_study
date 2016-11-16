#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
# ThreadLocal 一个线程安全的,在单个线程中共享的全局变量
import threading
localObj=threading.local()

def process1():
    dbconn=localObj.dbconn
    print('Db conn is %s current threading is %s' % (dbconn, threading.current_thread().name))

def process_thread(name):
    localObj.dbconn=name
    process1()

t1=threading.Thread(target=process_thread, args=('127.0.0.1',),name='北京机房')
t2=threading.Thread(target=process_thread, args=('192.54.2.132',),name='上海机房')
t1.start()
t2.start()
t1.join()
t2.join()
