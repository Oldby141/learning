class Role:
    n = 123#类变量
    list = []
    def __init__(self,name,weapen,money = 1500,ep = 100):
        #构造函数
        #在实例化时做一些类的初始化工作
        self.name = name#r1.name = name实例变量（静态属性），作用域就是实例本身
        self.weapen = weapen
        self.money = money
        self.__ep = ep#私有属性

    def __del__(self):
        print("%s died "%self.name)

    def got_shot(self):#类的方法功能 （动态属性）
        self.__ep -= 10
        print("name:%s I got_shot"%self.name)
        print("name:%s ep:%s"%(self.name,self.__ep))


    def buy_gun(self,gun_name):
        print("%s just bought %s"%(self.name,gun_name))

r1 = Role("byf","police","AK47")# 把一个类变成一个具体对象的过程叫实例化（初始化一个类，造了一个对象）
r1.buy_gun("AK47")
r1.got_shot()
print(r1.n)
r1.n = 12
print(Role.n)
print(r1.n)
r1.list.append("r1")
r2 = Role("alx","police","b51")
r2.list.append("r2")
print(r1.list,r2.list,Role.list)

