import time

print(time.clock())#返回处理器时间
print(time.process_time())#f返回处理器计算时间
print(time.asctime()) #返回时间格式"Fri Aug 19 11:14:16 2016"
print(time.altzone)#返回与utc时间的时间差,以秒计算\
print(time.localtime())#返回本地时间 的struct time对象格式
print(time.gmtime(time.time()))#返回utc时间的struc时间对象格式
print(time.ctime())#Tue Mar 19 09:08:51 2019

# 日期字符串 转成  时间戳
string_2_struct = time.strptime("2016/05/22","%Y/%m/%d") #将 日期字符串 转成 struct时间对象格式
print(string_2_struct)
print(time.mktime(string_2_struct))

#将时间戳转为字符串格式
print(time.gmtime(time.time()-86640)) #将utc时间戳转换成struct_time格式
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()) ) #将utc struct_time格式转成指定的字符串格式   ##utc  世界标准时间


#时间加减
import datetime
print(datetime.datetime.now())
print(datetime.date.fromtimestamp(time.time())) # 时间戳直接转成日期格式
print(datetime.datetime.now() + datetime.timedelta(-3))#当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分
c_time  = datetime.datetime.now()
print(c_time.replace(minute=3,hour=2)) #时间替换

print(time.gmtime(time.time()))
print(time.altzone)#返回与utc时间的时间差,以秒计算\