__author__ = "Alex Li"
'''
#data = open("yesterday",encoding="utf-8").read()
f = open("yesterday2",'a',encoding="utf-8") #文件句柄
#a = append 追加

f.write("\nwhen i was young i listen to the radio\n")
data = f.read()
print('--read',data)

f.close()

'''




#f = open("yesterday2",'r+',encoding="utf-8") #文件句柄 读写  只能写在最后
#f = open("yesterday2",'w+',encoding="utf-8") #文件句柄 写读  只能写在最后  暂时没用
#f = open("yesterday2",'a+',encoding="utf-8") #文件句柄 追加读写
f = open("yesterday",'wb') #文件句柄  二进制文件
f.write("hello binary\n".encode())
f.close()
#f.truncate(10)#从给定位置处截断

# "U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）
#
# rU
# r+U

'''

print(f.encoding)

#print(f.flush())
print(dir(f.buffer) )
#high bige

count = 0
for line in f:
    if count == 9:
        print('----我是分割线----------')
        count += 1
        continue
    print(line)
    count +=1

#low loop

for index,line in enumerate(f.readlines()):
    if index == 9:
        print('----我是分割线----------')
        continue
    print(line.strip())
#for i in range(5):
#    print(f.readline())
'''
