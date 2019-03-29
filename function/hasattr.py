#!_*_coding:utf-8_*_
class test():
    name="xiaohua"
    def run(self):
        return "HelloWord"
t=test()
print(hasattr(t, "name"))#判断一个对象里面是否有name属性或者name方法，返回BOOL值，有name特性返回True， 否则返回False。
# 需要注意的是name要用括号括起来
# getattr(object, name[,default])获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。
# 需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，
# 可以在后面添加一对括号。
# >>> class test():
# ...     name="xiaohua"
# ...     def run(self):
# ...             return "HelloWord"
# ...
# >>> t=test()
# >>> getattr(t, "name") #获取name属性，存在就打印出来。
# 'xiaohua'
# >>> getattr(t, "run")  #获取run方法，存在就打印出方法的内存地址。
# <bound method test.run of <__main__.test instance at 0x0269C878>>
# >>> getattr(t, "run")()  #获取run方法，后面加括号可以将这个方法运行。
# 'HelloWord'
# >>> getattr(t, "age")  #获取一个不存在的属性。
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: test instance has no attribute 'age'
# >>> getattr(t, "age","18")  #若属性不存在，返回一个默认值。
# '18'
# >>>

# setattr(object, name, values)
# 给对象的属性赋值，若属性不存在，先创建再赋值。
# >>> class test():
# ...     name="xiaohua"
# ...     def run(self):
# ...             return "HelloWord"
# ...
# >>> t=test()
# >>> hasattr(t, "age")   #判断属性是否存在
# False
# >>> setattr(t, "age", "18")   #为属相赋值，并没有返回值
# >>> hasattr(t, "age")    #属性存在了
# True
# >>>


# 一种综合的用法是：判断一个对象的属性是否存在，若不存在就添加该属性。
# >>> class test():
# ...     name="xiaohua"
# ...     def run(self):
# ...             return "HelloWord"
# ...
# >>> t=test()
# >>> getattr(t, "age")    #age属性不存在
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: test instance has no attribute 'age'
# >>> getattr(t, "age", setattr(t, "age", "18")) #age属性不存在时，设置该属性
# '18'
# >>> getattr(t, "age")  #可检测设置成功
# '18'
# >>>