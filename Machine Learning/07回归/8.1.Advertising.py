import pandas as pd
from sklearn.model_selection import train_test_split
import pprint
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

if __name__ == "__main__":
    path = "8.Advertising.csv"
    # f = open(path)
    # x = []
    # y = []
    # for i,d in enumerate(f):
    #     if i == 0:
    #         continue
    #     d = d.strip()
    #     if not d:
    #         continue
    #     d = list(map(float,d.split(",")))
    #     x.append(d[1:-1])
    #     y.append(d[-1])
    # pprint.pprint(x)#对于数据结构比较复杂、数据长度较长的数据，适合采用pprint()打印方式
    # pprint.pprint(y)
    # x = np.array(x)
    # y = np.array(y)
    # # numpy读入
    # p = np.loadtxt(path, delimiter=',', skiprows=1)
    # print (p)
    # pandas读入
    data = pd.read_csv(path)    # TV、Radio、Newspaper、Sales
    x = data[['TV', 'Radio', 'Newspaper']]
    # x = data[['TV', 'Radio']]
    y = data['Sales']
    print (x)
    print (y)

    #绘制1
    # plt.plot(data["TV"],y,'ro',label="TV")
    # plt.plot(data["Radio"],y,"g^",label="Radio")
    # plt.plot(data['Newspaper'], y, 'mv', label='Newspaer')
    # plt.legend(loc="lower right")#右下角标签
    # plt.grid()#网格
    # plt.show()

    #绘制2
    # plt.figure(figsize=(9,12))#创建一个图像窗口.
    # plt.subplot(311)#表示将整个图像窗口分为3行1列, 当前位置为1
    # plt.plot(data["TV"],y,"ro")
    # plt.title("TV")
    # plt.grid()
    # plt.subplot(312)
    # plt.plot(data["Radio"],y,"g^")
    # plt.title('Radio')
    # plt.grid()
    # plt.subplot(313)
    # plt.plot(data['Newspaper'], y, 'b*')
    # plt.title('Newspaper')
    # plt.grid()
    # plt.tight_layout()
    # plt.show()

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
    linreg = LinearRegression()
    model = linreg.fit(x_train,y_train)
    print(model)#打印出model,回归系数和截距
    print(linreg.coef_)
    print(linreg.intercept_)
    #下面是用测试数据来拟合或者说预测
    y_hat = linreg.predict(np.array(x_test))

    t = np.arange(len(x_test))  # t是一个等差数列，长度为x_test的数量
    plt.plot(t, y_test, 'r-', linewidth=2, label='Test') # plot(x,y,颜色和标识，标识的宽度，标识名)
    plt.plot(t, y_hat, 'g-', linewidth=2, label='Predict')# plot(x,y,颜色和标识，标识的宽度，标识名)
    plt.legend(loc='upper right')  # legend是图示说明
    plt.grid()  # 网格显示
    plt.show()  # 图像显示



