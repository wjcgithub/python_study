#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
import socket

# 创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议，
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 提供主机和端口号建立连接
s.connect(('html.hotfive.cn', 80))
# 发送请求
s.send(b'GET / HTTP/1.1\r\nHost:html.hotfive.cn\r\nConnection:close\r\n\r\n')

# 开始接收数据
buffer = []
while True:
    # 限制每次最多接受1k字节
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
s.close()

# 处理响应头和HTML体
header, html = data.split(b'\r\n\r\n')
print(header.decode('utf-8'))
# 把接收的数据写入文件
with open('hotfive.html','wb') as f:
    f.write(html)