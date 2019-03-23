import time
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
def consumer(name):
    print("%s准备吃包子啦"%name)
    while True:
        baozi = yield
        print("包子[%s]来了，包子被[%s]吃了"%(baozi,name))

# c = consumer("byf")
# c.__next__()
# c.send(0)
#c.__next__()
def produce(name):
    c = consumer("byf")
    c.__next__()
    print("开始做包子")
    for i in range(10):
        time.sleep(1)
        print("%s做了一个包子"%name)
        c.send(i)

produce("mm")
