product_list=[
    ('Iphone',5000),
    ('MacPro',9000),
    ('Bike',500),
    ('watch',200),
    ('cofe',20),
]
shopping_list=[]
salary=input("请输入你的薪水")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("选择买的物品？")
        if user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice<len(product_list) and user_choice >=0:
                p_item=product_list[user_choice]
                if salary>=p_item[1]:#买得起
                    shopping_list.append(p_item)
                    salary-=p_item[1]
                    print("购买成功，剩余金额：\033[31;1m%s\033[0m" %(salary))
                else:
                    print("金额不足")
            else:
                print("商品不存在")
        elif user_choice == 'q':
            print("--------------------shopping list----------------------------------")

            print(shopping_list)
            print("你的剩余余额：",salary)
            exit()
        else:
            print("invalid option")


