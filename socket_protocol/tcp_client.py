#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
import socket,threading,time

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接指定主机的指定端口
s.connect(('127.0.0.1', 9991))

# 接受欢迎信息
print(s.recv(1024).decode('utf-8'))
for data in [b'lisi', b'wangwu', b'zhangsang']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
    time.sleep(2)
s.send(b'exit')
s.close()