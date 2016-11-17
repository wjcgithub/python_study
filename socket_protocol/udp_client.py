#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'zhangsan',b'lisi',b'wangwu']:
    s.sendto(data, ('127.0.0.1',9998))
    print(s.recv(1024).decode('utf-8'))
s.close()