import sys,os
print(sys.path)
print(os.path.abspath(__file__))
x = os.path.dirname(os.path.abspath(__file__))
print(x)
y = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(y)
sys.path.append(y)
#print(sys.path)
from day4 import module_test
#在"from YY import XX"这样的代码中，无论是XX还是YY，只要被python解释器视作package，
# 就会首先调用该package的__init__.py文件。如果都是package，则调用顺序是YY，XX。
import module_test2#运行该文件
#from . import module_test2
#另外，练习中“from . import XXX”和“from .. import XXX”中的'.'和'..'，
# 可以等同于linux里的shell中'.'和'..'的作用，表示当前工作目录的package和上一级的package。
#文件夹被python解释器视作package需要满足两个条件：
# 　　1、文件夹中必须有__init__.py文件，该文件可以为空，但必须存在该文件。
# 　　2、不能作为顶层模块来执行该文件夹中的py文件（即不能作为主函数的入口）。