#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import functools
int2=functools.partial(int,base=2)
int2(1234)

max2 = functools.partial(max, 10)