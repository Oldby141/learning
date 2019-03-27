#!_*_coding:utf-8_*_
class Dog(object):

    def __init__(self,name,food):
        self.name = name#调用的不是这个name
        self.__food = None
    #@staticmethod#实际上和类没关系了
    #@classmethod #没用过e
    @property
    def eat(self):
        print("%s is eating %s"%(self.name,self.__food))
    @eat.setter
    def eat(self,food):
        print('set ro food：',food)
        self.__food = food
    @eat.deleter #增加删除方法
    def eat(self):
        del self.__food

    def talk(self):
        print("%s is talking"%self.name)

d = Dog("A","b")
d.eat
d.eat  = 'f'
d.eat
del d.eat
# d.eat
# del d.name
# print(d.name)