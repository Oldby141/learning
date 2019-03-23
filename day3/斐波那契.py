def fib(max):
    n,a,b = 0,1,1
    while n < max:
        #print(b)
        yield b#返回函数当前值
        a,b = b,a+b#此处创建一个元组t = (b, a + b) # t是一个tuple，a = t[0]，b = t[1]
        n = n+1
    return  "done"
g = fib(3)
#fib(10)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# for i in f:
#     print(i)
