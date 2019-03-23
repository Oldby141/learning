from functools import reduce
def map_test(func,array):
    array_new=[]
    for i in array:
        array_new.append(func(i))
    return array_new
print (map_test(lambda x:x**2,range(10)))
print (list(map(lambda x:x**2,range(10))))

def odd(num):
    return num % 2
def filter_test(func,array):
    array_new=[]
    for i in array:
        if func(i):
            array_new.append(i)
    return array_new

print (filter_test(odd,range(10)))
print (list(filter(odd,range(10))))
# python filter()函数
# 描述：
# filter()函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，返回True或False，将返回True的元素放到新列表中。
# 语法：
# filter(function, iterable)
# 参数：
# function：判断函数
# iterable：可迭代对象
# 返回值：
# 列表
def reduce_test(func,array,init):
    l=list(array)
    if init is None:
        res=l.pop(0)
    else:
        res=init
    for i in l:
        res=func(res,i)
    return res

print( reduce_test(lambda x,y:x+y,range(10),10))
print(reduce(lambda x,y:x+y,range(100),10))#在 Python3 中，reduce() 函数已经被从全局名字空间里移除了，它现
# 在被放置在 functools 模块里，如果想要使用它，则需要通过引入 functools 模块来调用 reduce() 函数：