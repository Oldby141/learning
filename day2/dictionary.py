info={
    '101':"ss",
    '102':"sda",
    '103':"sas"
}
print(info.pop("101"))
print(info)
print(info.get('0'))
print('102' in info)
info["101"]="sda"

del info['101']
print(info)
#注意：key不要用  中文
c = dict.fromkeys([1,5,7,9,8],"test")#若改变其中的某一项值，全部项都改变
print(c)
print(info.items())

#循环输出建议用第一种：
for i in info:
    print(i,info[i])#更高效
for k,v in info.items():
    print(k,v)
info.setdefault("stu1102","龙泽萝拉")
print(info)