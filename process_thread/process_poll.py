#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
from multiprocessing import Pool
import os, time, random
import multiprocessing


def long_time_task(name):
    print('Run task %s (%s)....' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p=Pool(9)
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    print('Waitting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

# 获取cpu核数
print(multiprocessing.cpu_count())