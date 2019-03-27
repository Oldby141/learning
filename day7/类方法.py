#!_*_coding:utf-8_*_

class Dog(object):
    name = "zg"
    def __init__(self,name):
        self.name = name#调用的不是这个name
    #@staticmethod#实际上和类没关系了
    @classmethod #没用过
    def eat(self):
        print("%s is eating %s"%(self.name,'dd'))

    def talk(self):
        print("%s is talking"%self.name)

d = Dog("A")
d.eat()
