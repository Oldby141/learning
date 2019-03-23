def test(name,age=18,*args,**kwargs):#带*的要在后面
    print(name)
    print(age)
    print(args)
    print(kwargs)

test(1,2,3,4,**{'5':5})
test(1,2,3,4,li="s")#li不能是数字，s有引号，li没有