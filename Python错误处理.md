> 跟踪程序的执行，查看变量的值是否正确，这个过程称为调试。Python的pdb可以让我们以单步方式执行代码
> 异常捕获
> > try except finally
> > try except except... finally
> > try except except... else finally

> Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
https://docs.python.org/3/library/exceptions.html#exception-hierarchy

## 自定义错误
> 选择好继承关系后定义自己的错误类
> 手动抛出错误　`raise ErrorClass('error info')`