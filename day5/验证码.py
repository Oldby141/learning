import random

checkcode = ""
for i in range(4):
    current = random.randint(0,4)
    if current == i :
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print(checkcode)
