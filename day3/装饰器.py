import time
def timer(func):
    def deco():
        start_time=time.time()
        func()
        end_time = time.time()
        print("run time%s"%(end_time-start_time))
    return deco
@timer
def test1():
    time.sleep(2)
    print("in the test1")

def test2():
    time.sleep(2)
    print("in the test2")

#test1=timer(test1)
test1()

test2()
#https://blog.51cto.com/egon09/1836763?tdsourcetag=s_pctim_aiomsg装饰器详解

#迭代器
from collections import Iterable
from collections import Iterator
print(isinstance([],Iterable))#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
print(isinstance((i for i in range(10)),Iterator))#*可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
print(isinstance("ada",Iterator))#把list、dict、str等Iterable变成Iterator可以使用iter()函数