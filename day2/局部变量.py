name = "byf"

def changename(n):
    print("old name:",n)
    n = "byf nb"
    print("new name",n)

changename(name)
print(name)

def changename2(n):
    print("old name:",n)
    global  name##global不要用
    name= "byf nb"
    print("new name",n)

changename2(name)
print(name)

name2=[1,2,4,5]
def change(name):#列表，字典，集合可以改
    name[0]=0
change(name2)
print(name2)

name3=5
def changename3(name3):#数字字符串不能改（）全局变量值不变
    name3=2
    print(name3)
changename3(name3)
print(name3)