#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

#dict

# 赋值
d = {'zhangsan':13, 'lisi':45, 'wangwu':28}
d['wjc'] = 18

# 获取值
print(d)
print(d['wjc'])
print('wjc' in d)
if 'lisi' in d:
    print('lisi：'+str(d['lisi']))
else:
    print('lisi not exists!')

#通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('wangwu'))
print(d.get('wangermazi','wangermazi not exists!'))

# 删除
d.pop('lisi')
print(d)

# set
# 赋值  要创建一个set，需要提供一个list作为输入集合
s = set(list(range(10)))
s1 = set(['a','b','c'])
print(s)
print(s1)

# 添加
s1.add('d')
# s.add([8,9])  报错，不可传入可变元素，因为无法保证元素唯一性
s.add((1,2,3))   # 不报错
# s.add((1,2,3,[7,8]))  报错，不可传入可变[7,8]元素，因为无法保证元素唯一性

# 删除
s1.remove('a')

print(s1)

# 两个集合做交集 并集
print(s & s1)
print(s | s1)