#!_*_coding:utf-8_*_

# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#
#
# f = Foo("alex")
# print(type(f))
# print(type(Foo))

def func(self):
    print('hello %s'% self.name)
def __init__(self,name,age):
    self.name = name
    self.age = age

Foo = type('Foo',(object,),{'talk':func,'__init__':__init__})#
# #type第一个参数：类名
#type第二个参数：当前类的基类
#type第三个参数：类的成员
f = Foo('Chrn',22)
f.talk()
print(type(Foo))