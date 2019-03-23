print(round(3.14216,0))#保留小数
print(all([1,2,0]))
print(all("1234560"))
print(any([1]))
a = ascii([1,2,"lao"])#ascii() 函数类似 repr() 函数, 返回一个表示对象的字符串
print(type(a),[a])
a = bytes("5abcde",encoding="utf-8")#bytes 函数返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。它是 bytearray 的不可变版本。
# class bytes([source[, encoding[, errors]]])
# 参数
# 如果 source 为整数，则返回一个长度为 source 的初始化数组；
# 如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
# 如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
# 如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
# 如果没有输入任何参数，默认就是初始化数组为0个元素。
print(a[0])
b = bytearray("ab",encoding="utf-8")#bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的
print(b[1])
b[1] = 50
print(b)

print(a.capitalize(),a)
def sayhi():pass
print(callable((sayhi)))
calc = lambda n:3 if n<4 else n
print(calc(2))
print(globals())
def test():
    loca_var = 33
    print(locals())
test()

data = eval("3*3")#eval() 函数用来执行一个字符串表达式，并返回表达式的值。
print(data)