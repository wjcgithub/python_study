#多进程
## 类Unix系统使用os模块提供的fork函数
```python
import os
os.fork

```

## 跨平台版本的多进程模块
> 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，
> 因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去

- from multiprocessing import Process
- p=Process(target=子进程运行的函数, args=('一个元祖类型的参数',))
- p.start()  开始进程
- p.join     等待子进程结束

### Pool 进程池的使用
- 默认进程池容纳的数量是cpu的核数,可使用`multiprocessing.cpu_count()`查看

## python封装的子进程 `subprocess`
```Python
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
```

### 子进程需要输入的情况
```Python
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
```

## Python中的进程间通信
- Queue, Pipes, 信号量

### Queue的使用
```python
import Queue

q=Queue() 创建一个新队列
q.put 向队列中加入数据
q.get 从队列中读取数据
```

#多线程
> Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
> 由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。
> 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
> Python的threading模块有个current_thread()函数，它永远返回当前线程的实例
> 获取当前线程的名字使用`threading.current_thread().name`

```Python
t = threading.Thread(target=loop(线程执行的函数), name='LoopThread(线程的名字,方便查看,默认主线程是MainThread, 其他的线程如果不指定名字,就是Thread-1,Thread-2...)')  创建线程
t.start()  开启线程
t.join()   等待线程结束
```

## 线程的锁
> 因为同时运行的线程比较多,所以如果对于一个全局的变量,多个线程同时操作就要考虑锁的问题了
> python中使用`threading.Lock()`函数来提供锁的支持

```Python
lock = threading.Lock()  创建一个锁
def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
```

#如何使用线程安全的变量 `ThreadLocal`
> 实现在各个线程中维护自己的变量,不会和其他线程混淆,减少了进程中函数传递参数的繁琐问题,实际上在每个线程中就是自己的全局变量

```Python
localObj = threading.local()  返回一个对象,可以任意添加变量到其中
可以理解为全局变量localObj是一个dict，不但可以用localObj.student，还可以绑定其他变量，如localObj.teacher等等。
localObj.name = 'lisi'
localObj.age = 18'
```


# 分布式进程
- 通过multiprocessing的子模块managers将队列暴露到网络上, 这样生产者可以在一台机器跑,消费者可以在另一台机器上跑



# 总结
- 在Unix/Linux下，可以使用fork()调用实现多进程。
- 要实现跨平台的多进程，可以使用multiprocessing模块。
- 进程间通信是通过Queue、Pipes等实现的。
- 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
- Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。 如果必须使用多核cpu就要使用c开发扩展来实现了