#-*- coding:gb2312 -*-
#��python2Ĭ�ϱ�����ASCII, python3��Ĭ����unicode
# unicode ��Ϊ utf-32(ռ4���ֽ�),utf-16(ռ�����ֽ�)��utf-8(ռ1-4���ֽ�)�� so utf-16����������õ�unicode�汾�� �������ļ����Ļ���utf-8����Ϊutf8ʡ�ռ�
#��py3��encode,��ת���ͬʱ�����string ���bytes���ͣ�decode�ڽ����ͬʱ�����bytes���string
import sys
print(sys.getdefaultencoding())

s = "�Ұ������찲��"
s_gb2312 = s.encode("gb2312")
s_unicode = s_gb2312.decode("gb2312")
s_utf8 = s_gb2312.decode("gb2312").encode("utf-8")

print(s)
print(s_gb2312)
print(s_unicode)
print(s_utf8)