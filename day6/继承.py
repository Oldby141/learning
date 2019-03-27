#!_*_coding:utf-8_*_
# class People:#经典类
class People(object):#新式类写法  Object 是基类
    def __init__(self,name,age):
        self.name =  name
        self.age = age
        self.friends = []
        print("Run in People")

    def eat(self):
        print("%s is eating...."%self.name)

    def talk(self):
        print("%s is talking...." % self.name)

    def sleep(self):
        print("%s is sleeping...." % self.name)

class Relation(object):
    def __init__(self,name,age):
        print("Run in Relation")# 多继承先左后右
    def make_friend(self,obj):
        print("%s is making friends with %s"%(self.name,obj.name))
        #self.friends.append(obj.name)
        self.friends.append(obj)

class Man(Relation,People):
    def __init__(self,name,age,money):
        #People.__init__(self,name,age)
        super(Man,self).__init__(name,age)#新式类写法
        self.money = money
        print("出生的钱数目：%s"%self.money)
    def p(self):
        print("%s "%self.name)

    def sleep(self):
        People.sleep(self)
        print("man is sleeping")

class Woman(People,Relation):
    def get_birth(self):
        print("%s get birth"%self.name)

m1 = Man("byf",23,10)
# print(m1.name)
# m1.sleep()
w1 = Woman("gg",23)
# w1.get_birth()
#m1.make_friend(w1)
#print(m1.friends)
#print(m1.friends[0].name)
w1.name = "GG"
#print(m1.friends[0].name)