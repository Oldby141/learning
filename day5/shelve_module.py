import shelve
#import configparser
import datetime
d = shelve.open('shelve_test')  # 打开一个文件
print(d.get("name"))
print(d.get("info"))
print(d.get("date"))

# info =  {'age':22,"job":'it'}
#
# name = ["alex", "rain", "test"]
# d["name"] = name  # 持久化列表
# d["info"] = info  # 持久dict
# d['date'] = datetime.datetime.now()
# d.close()
#shelve是一额简单的数据存储方案，他只有一个函数就是open()，这个函数接收一个参数就是文件名，
# 并且文件名必须是.bat类型的。然后返回一个shelf对象，你可以用他来存储东西，就可以简单的把他当
# 作一个字典，当你存储完毕的时候，就调用close函数来关闭

#注意：
# list = [1, 2, 3]
#
# she = shelve.open('test.dat')
# she['d'] = list
# she['d'].append('f')print(she['d'])
# 你会发现，打印后，没有‘f’ ，存储的f到哪里去了呢？其实很简单，d没有写回，你把[1,2,3]存到了d，当你再次读取she['d']的时候，
# she['d']只是一个拷贝，而你没有将拷贝写回，所以当你再次读取she['d']的时候，
# 它又从源中读取了一个拷贝，所以，你新修改的内容并不会出现在拷贝中，解决的办法就是，第一个是利用一个缓存的变量，如下所示
# list = [1, 2, 3]
#
# she = shelve.open('test.dat')
# she['d'] = list
# temp = she['d']
# temp.append('f')
# she['d'] = temp
# print(she['d'])