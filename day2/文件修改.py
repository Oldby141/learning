f = open("yesterday",'r',encoding="UTF-8")
#f_new = open("yesterday2","w",encoding="UTF-8")

for line in f:
    if "肆意的快乐" in line:
        print('s')
        line=line.replace("肆意的快乐","s")#########888888888888******
        print(line)

f.close()
#f_new.close()

line="肆意的快乐"
print(line.replace("肆意的快乐","s"))
s=line.replace #s发生变化
print(line)##line没有发生变化

with open("yesterday","r",encoding="UTF-8") as f:
    for line in f:
        print(line.strip())
    print(f.tell())