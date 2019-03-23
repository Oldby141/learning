f = open("text.text","r")
data = eval(f.read())#eval() 函数用来执行一个字符串表达式，并返回表达式的值
print(data["age"])