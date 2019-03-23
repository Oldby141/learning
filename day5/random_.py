#_*_encoding: utf-8_*_
import random#注意模块名不能与文件名相同
print (random.random())  #0.6445010863311293
#random.random()用于生成一个0到1的随机符点数: 0 <= n < 1.0
print(random.randrange(1,10))
#random.randrange的函数原型为：random.randrange([start], stop[, step])，
# 从指定范围内，按指定基数递增的集合中 获取一个随机数。如：random.randrange(10, 100, 2)，
# 结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。
# random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效。
print (random.randint(1,7)) #4
#random.randint()的函数原型为：random.randint(a, b)，用于生成一个指定范围内的整数。
# 其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
print(random.choice('liukuni')) #i
#random.choice从序列中获取一个随机元素。
print(random.sample([1,2,3,4,5],3))    #[1, 2, 5]
#random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。


import string
#随机整数：
print( random.randint(0,99))  #70

#随机选取0到100间的偶数：
print(random.randrange(0, 101, 2)) #4

#随机浮点数：
print( random.random()) #0.2746445568079129
print(random.uniform(1, 10)) #9.887001463194844

#随机字符：
print(random.choice('abcdefg&#%^*f')) #f

#多个字符中选取特定数量的字符：
print(random.sample('abcdefghij',3)) #['f', 'h', 'd']

#随机选取字符串：
print( random.choice ( ['apple', 'pear', 'peach', 'orange', 'lemon'] )) #apple
#洗牌#
items = [1,2,3,4,5,6,7]
print(items) #[1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
print(items)