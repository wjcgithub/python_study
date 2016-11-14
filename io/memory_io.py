#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'

from io import StringIO

# 　可以初始化
f = StringIO('Hello!\nHi!\nGoodbye!')
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

from io import BytesIO

# 初始化
f = BytesIO()
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# print(dir(io))
#
f = StringIO()
# f.write('hello')
# ['BlockingIOError', 'BufferedIOBase', 'BufferedRWPair', 'BufferedRandom', 'BufferedReader', 'BufferedWriter', 'BytesIO', 'DEFAULT_BUFFER_SIZE', 'FileIO', 'IOBase', 'IncrementalNewlineDecoder', 'OpenWrapper', 'RawIOBase', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'StringIO', 'TextIOBase', 'TextIOWrapper', 'UnsupportedOperation', '__all__', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_io', 'abc', 'open']
