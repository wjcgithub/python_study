#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
# 需要python > 3.5

import asyncio

async def hello():
    print('hello world')
    r=await asyncio.sleep(1)
    print('hello again')

# 获取EventLoop:
loop=asyncio.get_event_loop()
# 执行coroutine
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()