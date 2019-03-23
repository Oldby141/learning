def re(n):
    print(n)
    if n>0:
        return  re(n//2)
    print("-->",n)

re(10)