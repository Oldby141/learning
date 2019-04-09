#!_*_coding:utf-8_*_
while True:
    try:
        a, matrix = int(input()), []
        for i in range(a):
            matrix.append(input().split())
        res=True
        for i in range(a):
            for j in range(a):
                if matrix[i][j]!=matrix[j][i]:
                    res=False
                    break
        print("Yes!" if res else "No!")
    except:
        break

while True:
    try:
        list1=[]
        list2=[]
        for i in range(2):
            line1=list(map(int,input().split()))
            list1.append(line1)
        for i in range(3):
            line2=list(map(int,input().split()))
            list2.append(line2)
        #print(list1,list2)
        sum1=int(list1[0][0])*int(list2[0][0])+int(list1[0][1])*int(list2[1][0])+int(list1[0][2])*int(list2[2][0])
        sum2=int(list1[0][0])*int(list2[0][1])+int(list1[0][1])*int(list2[1][1])+int(list1[0][2])*int(list2[2][1])
        sum3=int(list1[1][0])*int(list2[0][0])+int(list1[1][1])*int(list2[1][0])+int(list1[1][2])*int(list2[2][0])
        sum4=int(list1[1][0])*int(list2[0][1])+int(list1[1][1])*int(list2[1][1])+int(list1[1][2])*int(list2[2][1])
        print('%d %d \n%d %d '%(sum1,sum2,sum3,sum4))
    except:
        break