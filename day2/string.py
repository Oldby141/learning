s = " my name is {name}"
l=['z','s','a']

print(s.count("y"))
print(s.capitalize())#首字母大写
#print(s.casefold("a"))#大写全部变小写
#print(s.center(50，'-'))#填充居中
#print(s.encode())字符串转进制
print(s.endswith("YF"))
print(s.expandtabs(tabsize=30))
print(s.find("n"))
print(s.format(name="byf"))
#print(s.format_map({'name':byf}))
print(s.index("n"))
print('2'.isalnum())
print('s'.isalpha())
print('2341'.isdecimal())
print('324.2'.isdigit())#整数
print(' _ada'.isidentifier())#是否是合法标识符
print(s.islower())
#print(s.isnumeric())数字
#print(s.isprintable())#暂时不需要考虑
print('aaf32#'.isalnum())
print("My Name".istitle())
print("MFI".isupper())
print(''.join(l))#列表转字符串
#print(s.ljust(50，'*'))#右边填充
print('FSF'.lower())
print(s.lstrip(" m"))#左边去除字符“ m”
#print(s.maketrans())
#print(s.partition(5))
print(s.replace("name","byf",1))
print(s.rindex("n"))
print(s.rjust(50,'#'))
#print(s.rpartition('m'))
print(s.split(' '))
print("mad\nsad".splitlines())
print(s.startswith(" "))
#print(s.swapcase())#大小写互变
print(s.title())
#print(s.translate(" "))
print(s.upper())
#print(s.zfill(50))#用0填充
print('2'.encode(encoding='UTF-8',errors='strict'))#Python encode() 方法以 encoding 指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
p = str.maketrans("abcdef","123456")#对应转换
print('a'.translate(p))
print( "this is\tstring example....wow!!!".expandtabs(tabsize=15))#expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8
print("\tthis is\tstring example....wow!!!")
print(s.casefold())