#-*- coding:gb2312 -*-
#在python2默认编码是ASCII, python3里默认是unicode
# unicode 分为 utf-32(占4个字节),utf-16(占两个字节)，utf-8(占1-4个字节)， so utf-16就是现在最常用的unicode版本， 不过在文件里存的还是utf-8，因为utf8省空间
#在py3中encode,在转码的同时还会把string 变成bytes类型，decode在解码的同时还会把bytes变回string
import sys
print(sys.getdefaultencoding())

s = "我爱北京天安门"
s_gb2312 = s.encode("gb2312")
s_unicode = s_gb2312.decode("gb2312")
s_utf8 = s_gb2312.decode("gb2312").encode("utf-8")

print(s)
print(s_gb2312)
print(s_unicode)
print(s_utf8)