#!/usr/bin/env python3
# -*- coding:utf-8 -*-
print('start', "%2d-%02d" %(3,1),'end')
# %d
# %f
# %s
# %x

s1=72
s2=85

s3=(s2/s1-1)*100
s4=(s2-s1)/s1*100
print('%.1f%%' %(s3))
print('%.1f%%' %(s4))