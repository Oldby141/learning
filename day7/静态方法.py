#!_*_coding:utf-8_*_
class Dog(object):
    def __init__(self,name):
        self.name = name
    @staticmethod
    def eat(self):#实际上和类没关系了
        print("%s is eating %s"%(self.name,'dd'))

    def talk(self):
        print("%s is talking"%self.name)

d = Dog("A")
d.eat(d)
d.talk()