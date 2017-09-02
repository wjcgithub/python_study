# Python 资料与文档
1. 内置函数：https://docs.python.org/3/library/functions.html

# 常用数据成分
- int
- string
- float
- list
`L = [1,2,3]`
- tuple
`T = (1,2,3,[4,5])`
`tuple一旦初始化就不能修改`
- dict
`d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}`
- set 
`s = set(list(range(10)))`
`s1 = set(['a','b','c'])`

# 运算成分
- \+
- \-
- \*
- /
- //  下取整
- %

# 控制循环成分
- if
- while
- for in


# 输入输出成分
## 输入
- scanf

## 输出
- print()会依次打印每个字符串，遇到逗号“,”会输出一个空格
`print('a','b','c')`
`print('my name is '+str(name)+'!')`
- 单引号
- r``
- 双引号
- 三引号
- 转译字符

## 格式化输出
- %d
- %f
- %s
- %x

```
print('start', "%2d-%02d" %(3,1),'end')
s1=72
s2=85
s3=(s2/s1-1)*100
print('%.1f%%' %(s3))
```

# 函数
## 函数参数
- 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

比如定义一个函数，包含上述若干种参数：
```python
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
```
- 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
```python
>>> f1(1, 2)
a = 1 b = 2 c = 0 args = () kw = {}
>>> f1(1, 2, c=3)
a = 1 b = 2 c = 3 args = () kw = {}
>>> f1(1, 2, 3, 'a', 'b')
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
>>> f1(1, 2, 3, 'a', 'b', x=99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
>>> f2(1, 2, d=99, ext=None)
a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
```

- 最神奇的是通过一个tuple和dict，你也可以调用上述函数：
```python
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
```

## 函数返回值
- 定义函数时，需要确定函数名和参数个数；
- 如果有必要，可以先对参数的数据类型做检查；
- 函数体内部可以用return随时返回函数结果；
- 函数执行完毕也没有return语句时，自动return None。
- 函数可以同时返回多个值，但其实就是一个tuple。
- 默认参数要牢记一点：默认参数必须指向不变对象！
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
要注意定义可变参数和关键字参数的语法：
`*args`是`可变参数`，args接收的是一个`tuple`；
`**kw`是`关键字参数`，kw接收的是一个`dict`。
以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

# 高级特性
## 切片
- python 切片可以对list,tuple,字符串进行切片
- 记住倒数第一个元素的索引是-1
```python
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[:])  # 全切
print(L[:3:2])  # 指定范围并跳跃切，步值2
print(L[::2])  # 全切，步值2
print(L[1:2])  # 正向段落切
print(L[-2:]) # 倒着切
print(L[-1:])  # 切最后一个
```

## 迭代
- 字典dict的迭代
```python
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
  print(key)
```
> 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()

- 字符串迭代
```python
for ch in 'ABC':
    print(ch)
```
> 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型
> 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断

```python
from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代
#True
isinstance([1,2,3], Iterable) # list是否可迭代
#True
isinstance(123, Iterable) # 整数是否可迭代
#False
```

- list带下标的迭代
```python
for i, value in enumerate(['A', 'B', 'C']):
   print(i, value)
#0 A
#1 B
#2 C
```

```python
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
    
#1 1
#2 4
#3 9
```

## 生成式与生成器
- 生成式使用 `[]`
```python
#e3
L=[x*x for x in range(1,11)]
print(L)

#e4
L=[x*x for x in range(1,11) if x%2 == 0]
print(L)

#e5
L=[x*x for x in range(1,11) if x%2 == 1]
print(L)

#e6
L=[m+n for m in 'ABC' for n in 'XYZ']
print(L)

#e7
L=[d for d in os.listdir('.')]
print(L)
```

- 生成器使用 `()

### 生成器的第一种实现　`()`
- 第一种生成器的实现就是将生成式的`[]`改为`()`

```python
g = (x * x for x in range(10))
```

### 生成器的第二种实现　`yield关键字`
- 第二种生成器的方式就是在函数中使用`yield`关键字

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
```

### 生成式与生成器的区别

- `生成式`占用内存大，一次性创建所有的数据到内存中
- `生成器`占用的内存小，因为生成器存放到内存中的是算法本身，整的元素是取一次算一次的，所以比较剩内存

## 迭代器

> 可以被next()函数调用并不断返回下一个值的对象称为迭代器：`Iterator`
> 可以使用isinstance()判断一个对象是否是Iterator对象
```python
from collections import Iterator
isinstance((x for x in range(10)), Iterator)
```
> 生成器都是Iterator对象，但`list`,`dict`,`str`虽然是`Iterable`，却不是`Iterator`。
> 把`list`,`dict`,`str`等`Iterable`变成`Iterator`可以使用`iter()`函数

#函数式编程

> 函数也是一个对象
> 而且函数对象可以被赋值给变量，所以，通过变量也能调用函数

##高阶函数

> 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为`高阶函数`

###map/reduce

> 我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
`list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))`
> reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
`reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)`

###filter

> 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

```python
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
[1, 5, 9, 15]
```

###sorted
> sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
> key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
> 默认情况下，对字符串排序，是按照ASCII的大小比较的
`sorted(L,key=func_name,reverse=True|False)`

##返回函数
> 就是将函数的返回值由原来的返回基本数据类型改为返回函数，但是该函数不会立即执行

### 注意闭包
> 返回函数不要引用任何循环变量，或者后续会发生变化的变量

```python
#closure
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3=count()
print(f1())
print(f2())
print(f3())


def count():
    def f(j):
        def p():
            return j*j
        return p
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3=count()
print(f1())
print(f2())
print(f3())
```

##匿名函数
> 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
> 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
```python
lamada: x,y:x*x+y*y
```

##装饰器
`link:` http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000

##偏函数
> 偏函数（Partial function）
> 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
> 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单

```python
import functools
int2 = functools.partial(int, base=2)
int2('1000000')
int2('1010101')
```


#模块

> python中的模块名就是文件名
> 模块还可以有层级结构
> 带目录的模块，内部必须有`__init__.py`文件，他代表的就是当前这个目录的模块，表示模块`dirname.filename(模块名称)`　｜　`dirname.dirname......filename(模块名)`
> 如果有多层目录结构，那么每层目录里面都要有一个`__init__.py`文件
> 自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。

##导入模块
```
from PIL import Image
import sys
```

##模块搜索目录
使用`sys.path`显示模块的加载路径

###修改模块的加载路径
1. 一是直接修改sys.path，添加要搜索的目录：  `sys.path.append('/Users/michael/my_py_scripts')` 这种方法是在运行时修改，运行结束后失效。
2. 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

# 面向对象编程 
- 不同点和phpd的面向对象比较

> 使用class声明变量
> 继承　`class Student(Object)`
> 调用属性和方法使用`.`, 不使用`->`
> 构造函数为`__init__`
> 函数的第一个参数默认为`self`    funcname(self(python固定),其他和普通函数一样的参数)

## 访问权限
1. 什么都不修饰就是公有的属性     name
2. 变量前面添加__就是私有属性　　　__name
3. 前后都添加__的是特殊变量,可以直接访问＝　　　　__name__
4. 你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
5. 

##获取对象信息

```python
class Animal(object):
    name="金毛"
    
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running')

class Cat(Animal):
    def run(self):
        print('Cat is running')


cat=Cat()
dog=Dog()

print(type(cat))
print(type(dog))

print(isinstance(cat,Cat))
print(isinstance(cat,Animal))
print(isinstance(cat,Dog))


print(isinstance([1,2,3], (list,tuple)))
print(isinstance((1,2,3), (list,tuple)))

print(dir(dog))
print(dir('ABC'))


print(hasattr(dog,'name'))
print(getattr(dog,'name'))
setattr(dog,'name','比熊')
print(getattr(dog,'name'))
print(getattr(dog,'color', '黄色'))

returnrun = getattr(dog, 'run')
returnrun()
```

##实例属性和类属性

> Python中oop的属性分为类属性和实例属性，一个实例可以在外部在声明多个实例属性
> 实例属性不会覆盖类属性，这点需要注意

```python
class Student(object):
    name='Student'

s=Student()
print(s.name)             # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name)       # 打印类的name属性


s.name="Lisi"
print(s.name)              # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name)        # 但是类属性并未消失，用Student.name仍然可以访问

del s.name                 # 如果删除实例的name属性
print(s.name)              # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

```

> 在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

# 面向对象高级编程
## slots
> 规定python类只能具有某些属性，但是__slots__定义的属性仅仅对当前类实例起作用，对继承的子类是不起作用的
> 除非在子类中也定义__slots__，这样子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
> 用tuple定义允许绑定的属性名称

```python
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
```

## @property
> 为了解决在类外随意修改类的属性而产生的一个语法糖，他通过实现一个属性的set,get方法类实现一个属性的能力，这样属性的赋值通过内部定义的方法就可以实现控制判断操作了
> Python内置的@property装饰器就是负责把一个方法变成属性调用的

```python
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
```

> birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

```python
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
```

## 多重继承
> python支持多重继承，（php支持单继承多接口，但是可用trait提供多重继承的功能）
> MixIn的目的就是给一个类增加多个功能
> python的多重继承是通过`,`分隔

```python
class A(B,C,D,EMixIn)
```

## Python定制类（类似php中的魔术方法）
1. `__str__`
2. `__repr__`
3. `__iter__`
4. `__next__`
5. `__getitem__`
6. `__getattr__`
7. `__call__`

> 对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限

# 枚举类
> Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较

# I/O
> python的i/o和c的用法是兼容的

## I/O函数
open
close
readline
readlines 返回list集合

## 读取参数
open(filename,类型(r|rb),encoding=(gbk|utf-8),errors='ignore'))

## 内置关闭文件句柄描述付
```
with open('a.txt','r') as f:
    print(f.read())
```

## StringIO, BytesIO
> StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
read
readline
write
getvalue

## 序列化pickling，反序列化unpickling
> 依赖的模块pickle
> pickle.dumps(dict)  序列化为二进制
> pickle.dump()       直接把对象序列化后写入一个file-like Object
> pickle.load(bytes)  从一个file-like Object中直接反序列化

# 爬虫
https://jecvay.com/category/smtech/python3-webbug
http://blog.csdn.net/nwpulei/article/details/8457738
