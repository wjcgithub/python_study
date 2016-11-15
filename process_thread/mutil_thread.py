#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
import time, threading


# 线程要执行的代码
def loop():
    print('thread %s is  running...' % threading.current_thread().name)
    n = 0
    while n < 5:
       n=n+1
       print('thread %s >>> %s ' % (threading.current_thread().name, n))
       time.sleep(1)
    print('thread % s ended.' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t=threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


# 多线程的共享变量问题
# 假定这是你的银行存款, 只要在足够多的请求次数执行后,balance就不一定0了,
# 原因是系统处理运算的时候是有中间变量这个变量是存在寄存器中的,
# 就相当于两个变量做交换数据一样,需要第三个变量来做中间值(当然这里只考虑使用中间变量,不考虑其他方法),
# 这样如果系统执行到了一半发生了中断操作,就会出现计算错误的

balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# 将上面的操作加上lock控制
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)