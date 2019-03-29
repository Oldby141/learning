#!_*_coding:utf-8_*_
class Dog(object):
    '''描述类信息'''

    def __init__(self,name,food):
        self.name = name#调用的不是这个name
        self.__food = food#None
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

    def __call__(self, *args, **kwargs):
        print("runing call%s%s"%(args, kwargs))
    def __str__(self):#重写__str__
        return '<obj:%s>'%self.name

print(Dog.__doc__)#打印注释
d = Dog('d','b')
d(123,name=5)
print(Dog.__dict__)#打印类中所有属性，不包括实力属性
print(d.__dict__)#打印所有实例属性，不包括类属性
print(d.__str__())
