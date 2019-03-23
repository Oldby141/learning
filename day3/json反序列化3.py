import json

f = open("text.text","r")

#data = json.loads(f.read()) #data = pickle.loads(f.read())

for line in f:#json是一行一行处理数据的，若一次性加载在内存中，读取时后面的一行会覆盖前面的一行。所以要循环遍历输出
     print(json.loads(line))
#print(json.loads(f.read()))#文件中有多行时会报错
########￥￥￥￥￥￥********在存储文件过程中不能有空行，若是自己往文件中手动存储字典类型的数据，就要全部引用双引号！！！！！！
# https://www.cnblogs.com/haishiniu123/p/6775510.html区别与联系