#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'

# Python中的序列化
import pickle
d={'name':'lsii','age':12}
serialize=pickle.dumps(d)  #dump -> file-like object
print(serialize)

d2=pickle.loads(serialize)  # loads -> file-like object to dict
print(d2)

# Python中的json
import json
d={'name':'lsii','age':12}
str=json.dumps(d)
print(str)
print(type(str))
print(json.loads(str))
print(type(json.loads(str)))

