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

## 单元测试
> 需要继承`unittest.TestCase`
> `test_`开头的方法都是测试方法，自动执行
1. 断言等于  assertEqual
2. 断言抛出指定类型的Error    assertRaises

## 运行单元测试
1. 最简单的运行方式是在mydict_test.py的最后加上两行代码
```python
if __name__ == '__main__':
    unittest.main()
```
运行：`$ python3 mydict_test.py`

2. 命令行运行
```python
$ python3 -m unittest mydict_test
```

## setUp tearDown
可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行,比如链接数据库

- 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
- 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
- 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
- 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。