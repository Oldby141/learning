import time
def a():
    time.sleep(2)
    print("in the a")

def test(fun):
    print(fun)
    return fun#此处不要写为func()

a=test(a)
#a()