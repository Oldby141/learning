#!_*_coding:utf-8_*_
name = ['a','b']
dta = {}

try:
    name[3]#IndentationError缩进错误捕获不到
    open("tes.txt")
except(KeyError,IndexError) as e:
    print("没有这个key",e)
except Exception as e:
    print("未知错误",e)
else:
    print("y一切正常")
finally:
    print("不管有没有错，都执行")