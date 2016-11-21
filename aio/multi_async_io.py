#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
import asyncio,threading

@asyncio.coroutine
def hello():
    print('Hello world! (%s)', threading.current_thread().name)
    # 异步调用asyncio.sleep(1):
    r=yield from asyncio.sleep(2)
    print('Hello again! (%s)', threading.current_thread().name)

# 获取EventLoop:
loop=asyncio.get_event_loop()
# 执行coroutine
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()