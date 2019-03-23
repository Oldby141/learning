import time

def a():
    time.sleep(2)
    print("in the a")

def f(fun):
    start_time=time.time()
    #fun()
    end_time=time.time()
    #print("run time:%s"%(end_time-start_time))

a()
f(a)#注意不要写成f(a()),带括号是将a()函数运行结果作为参数传入

# 高阶函数：
#
# a.把一个函数名当做实参传给另一个函数（在不修改被装饰函数源代码的情况下为其添加功能）
# b.返回值中包含函数名（不修改函数调用方式）