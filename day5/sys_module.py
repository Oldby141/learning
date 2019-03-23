import sys
print(sys.argv)#命令行参数List，第一个元素是程序本身路径
print("sss sss")
print(sys.version)#获取Python解释程序的版本信息
print(sys.maxsize)
print(sys.path)
print(sys.platform)#返回操作系统平台名称
sys.stdout.write("a")
val = sys.stdin.readline()#input()方法和stdin()类似，不同的是input()括号内可以直接填写说明文字。
print(val)
sys.exit(0)#退出程序，正常退出时exit(0)
print("sss")