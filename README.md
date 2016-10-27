# python_study

## 输入输出
### 输入
- scanf

### 输出
- print()会依次打印每个字符串，遇到逗号“,”会输出一个空格
`print('a','b','c')`
`print('my name is '+str(name)+'!')`
- 单引号
- r``
- 双引号
- 三引号
- 转译字符

### 格式化输出
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

## 常用数据类型
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

## 运算符
- \+
- \-
- \*
- /
- //  下取整
- %

## 控制循环成分
- if
- while
- for in

## 函数
### 函数参数
- 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

### 函数返回值
- 定义函数时，需要确定函数名和参数个数；
- 如果有必要，可以先对参数的数据类型做检查；
- 函数体内部可以用return随时返回函数结果；
- 函数执行完毕也没有return语句时，自动return None。
- 函数可以同时返回多个值，但其实就是一个tuple。
- 默认参数要牢记一点：默认参数必须指向不变对象！
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
要注意定义可变参数和关键字参数的语法：
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。