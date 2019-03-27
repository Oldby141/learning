l = []
r = []
x = []
r.append(l)
print(r[0])
def a(l):
    for j in range(3):
        l.append(j)
    r.append(l)
    print(r[0])
    x.append(list(l))
    if len(l)<20:
        a(l)

a(l)
print(r)
print(x)
