#!_*_coding:utf-8_*_
import numpy as np
a=[[1,2,3],
   [4,5,6]]
print("列表a如下：")
print(a)

print("增加一维，新维度的下标为0")
c=np.stack(a,axis=0)
print(c)

print("增加一维，新维度的下标为1")
c=np.stack(a,axis=1)
print(c)

a=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12]]
print("列表a如下：")
print(a)

print("增加一维，新维度的下标为0")
c=np.stack(a,axis=0)
print(c)

print("增加一维，新维度的下标为1")
c=np.stack(a,axis=1)
print(c)

a=[1,2,3,4]
b=[5,6,7,8]
c=[9,10,11,12]
print("a=",a)
print("b=",b)
print("c=",c)

print("增加一维，新维度的下标为0")
d=np.stack((a,b,c),axis=0)
print(d)

print("增加一维，新维度的下标为1")
d=np.stack((a,b,c),axis=1)
print(d)

a=[[1,2,3],
   [4,5,6]]
b=[[1,2,3],
   [4,5,6]]
c=[[1,2,3],
   [4,5,6]]
print("a=",a)
print("b=",b)
print("c=",c)

print("增加一维，新维度的下标为0")
d=np.stack((a,b,c),axis=0)
print(d)

print("增加一维，新维度的下标为1")
d=np.stack((a,b,c),axis=1)
print(d)
print("增加一维，新维度的下标为2")
d=np.stack((a,b,c),axis=2)
print(d)
##############################################hstack()函数######它其实就是水平(按列顺序)把数组给堆叠起来
a=[1,2,3]
b=[4,5,6]
print(np.hstack((a,b)))

a=[[1],[2],[3]]
b=[[1],[2],[3]]
c=[[1],[2],[3]]
d=[[1],[2],[3]]
print(np.hstack((a,b,c,d)))
##############################################vstack()函数######参数tup可以是元组，列表，或者numpy数组，返回结果为numpy的数组。看下面的代码体会它的含义
a=[1,2,3]
b=[4,5,6]
print(np.vstack((a,b)))

a=[[1],[2],[3]]
b=[[1],[2],[3]]
c=[[1],[2],[3]]
d=[[1],[2],[3]]
print(np.vstack((a,b,c,d)))
#它是垂直（按照行顺序）的把数组给堆叠起来