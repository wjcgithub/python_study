#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'
import subprocess

print('$ nslookup www.python.org')
r=subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)