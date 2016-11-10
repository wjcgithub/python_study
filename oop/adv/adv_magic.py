#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Wangjichao'

#__str__    php: __toString      返回用户看到的字符串
#__repr__                        返回程序开发者看到的字符串
#__iter__  __next__              使用类来做迭代
#__getitem__                     获取指定项
#__getattr__                     访问不存在的属性时候调用
#__call__                        对实例进行直接调用就好比对一个函数进行调用一样

#__iter__, __next__
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>100:
            raise StopIteration();
        return self.a

for n in Fib():
    print(n)


# __getitem__
class Fib1(object):
    def __getitem__(self, n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
f1=Fib1()
print(f1[5])

class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n,int):
            a,b=0,1
            for x in range(n):
                a,b=b,a+b
            return a

        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b=b,a+b
            return L

f2=Fib2()
print(f2[:8])


#__getattr__
class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return 100
        else:
            return '属性'+attr+'不存在'

s=Student()
print(s.age)
print(s.name)

#__getattr__当做函数调用
class Student1(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 100

s1=Student1()
print(s1.age())


#__getattr__ 链式操作
class Chain(object):
    def __init__(self,path=''):
        self.path=path
    def __getattr__(self, path):
        if path=='request':
            return lambda: 'http:/'+self.path+'/'+'cus_list'
        return Chain("%s/%s" % (self.path, path))
    def __str__(self):
        return self.path

    __repr__=__str__

chain=Chain()
print(chain.status.user.timeline.all.list.request())


#__call__
class C1(object):
    def __init__(self, name):
        self.name=name

    def __call__(self, *args, **kwargs):
        print('function name is %s' % self.name)

c=C1('haha')
c()

print(callable(c))
print(callable(chain))