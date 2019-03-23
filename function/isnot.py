x = []
y = None
print(not x is None)####################true
print(not y is None)#F
print(not x)#################true
print(not y)#True
print(x is None)#flase
print(y is None)#true
print(y == None)#true
x = 1
y = [0]
print(not x)#f
print(not y)#f
print(x is None)#f
print(y is None)#f
print(y == None)#f
x = 0
y = [1]
print(not x is None)#############################t
print(not y is None)#t
print(not x)#################true
print(not y)#f
print(x is None)#flase
print(y is None)#f
print(x == None)#f
print(True is None)#f

class foo(object):
    def __eq__(self, other):
        return True
f = foo()
print(f==None)#f
print(f is None)#f

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list1==list2#t
list1 is list#f
