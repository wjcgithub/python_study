#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 记住倒数第一个元素的索引是-1。

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[:])  # 全切
print(L[:3:2])  # 指定范围并跳跃切，步值2
print(L[::2])  # 全切，步值2
print(L[1:2])  # 正向段落切
print(L[-2:]) # 倒着切
print(L[-1:])  # 切最后一个
