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
- dist
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
```
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
```
- 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
```
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
```
>>> args = (1, 2, 3, 4)
>>> kw = {'d': 99, 'x': '#'}
>>> f1(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
>>> args = (1, 2, 3)
>>> kw = {'d': 88, 'x': '#'}
>>> f2(*args, **kw)
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
```
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
```
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
  print(key)
```
> 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()

- 字符串迭代
```
for ch in 'ABC':
    print(ch)
```
> 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型
> 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断

```
from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代
True
isinstance([1,2,3], Iterable) # list是否可迭代
True
isinstance(123, Iterable) # 整数是否可迭代
False
```

- list带下标的迭代
```
for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)
...
0 A
1 B
2 C
```

```
>>> for x, y in [(1, 1), (2, 4), (3, 9)]:
...     print(x, y)
...
1 1
2 4
3 9
```

## 生成式与生成器
- 生成式使用 `[]`
```
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
```

```

### 生成式与生成器的区别
- `生成式`占用内存大，一次性创建所有的数据到内存中
- `生成器`占用的内存小，因为生成器存放到内存中的是算法本身，整的元素是取一次算一次的，所以比较剩内存

## 迭代器
> 可以被next()函数调用并不断返回下一个值的对象称为迭代器：`Iterator`
> 可以使用isinstance()判断一个对象是否是Iterator对象
```
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

```
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
```

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
```
lamada x,y:x*x+y*y
```

##装饰器
`link:` http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000

##偏函数
> 偏函数（Partial function）
> 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
> 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单

```
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