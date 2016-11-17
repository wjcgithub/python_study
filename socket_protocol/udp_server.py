#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9998))

print('Bind UDP on 9998')
try:
    while True:
        data,addr=s.recvfrom(1024)
        if(not data or data=='exit'):
            break
        print('Received from %s:%s.' % addr)
        s.sendto(('Hello, '+data.decode('utf-8')).encode('utf-8'), addr)
    s.close()
finally:
    s.close()