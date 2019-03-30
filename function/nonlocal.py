#!_*_coding:utf-8_*_
def make_counter():
    count = 0

    def counter():
        nonlocal count#nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
        count += 1
        return count

    return counter


def make_counter_test():
    mc = make_counter()
    print(mc())
    print(mc())
    print(mc())


make_counter_test()
