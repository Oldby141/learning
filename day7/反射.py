#!_*_coding:utf-8_*_
def bulk(self):
    print("%s is yelling...." %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating..."%self.name,food)

b = Dog("b")
print(hasattr(b,"eat"))
choice = input(">>").strip()
if hasattr(b,choice):
    fun = getattr(b,choice)
    fun("food")
else:
    setattr(b,choice,bulk) #d.talk = bulk
    func = getattr(b, choice)
    func(b)