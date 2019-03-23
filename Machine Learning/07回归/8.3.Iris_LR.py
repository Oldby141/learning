#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import preprocessing#预处理
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline#组装几个可以交叉验证的步骤，同时设置不同的参数，管道是前一个输出是
# 下一个步骤的输入，管道中间步骤必须是转换，也就是说必须要实现拟合和转换方法）


def iris_type(s):
    it = {b'Iris-setosa': 0, b'Iris-versicolor': 1, b'Iris-virginica': 2}#加b是字符编码问题
    return it[s]


if __name__ == "__main__":
    path = u'8.iris.data'  # 数据文件路径

    # # # 手写读取数据
    # # f = open(path)
    # # x = []
    # # y = []
    # # for d in f:
    # #     d = d.strip()
    # #     if d:
    # #         d = d.split(',')
    # #         y.append(d[-1])
    # #         x.append(map(float, d[:-1]))
    # # print '原始数据X：\n', x
    # # print '原始数据Y：\n', y
    # # x = np.array(x)
    # # print 'Numpy格式X：\n', x
    # # y = np.array(y)
    # # print 'Numpy格式Y - 1:\n', y
    # # y[y == 'Iris-setosa'] = 0
    # # y[y == 'Iris-versicolor'] = 1
    # # y[y == 'Iris-virginica'] = 2
    # # print 'Numpy格式Y - 2:\n', y
    # # y = y.astype(dtype=np.int)
    # # print 'Numpy格式Y - 3:\n', y
    #
    # # 使用sklearn的数据预处理
    # df = pd.read_csv(path, header=0)
    # x = df.values[:, :-1]#注意中间是，
    # y = df.values[:, -1]
    # print ('x = \n', x)
    # print ('y = \n', y)
    # le = preprocessing.LabelEncoder()
    # le.fit(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
    # print (le.classes_)
    # y = le.transform(y)
    # print ('Last Version, y = \n', y)
    #
    # # 路径，浮点型数据，逗号分隔，第4列使用函数iris_type单独处理
    data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_type})
    print( data)
    # 将数据的0到3列组成x，第4列得到y
    x, y = np.split(data, (4,), axis=1)#axis=1表示列  （4，）表示划分为前三列和之后

    # 为了可视化，仅使用前两列特征
    x = x[:, :2]
    #
    # x = StandardScaler().fit_transform(x)
    # lr = LogisticRegression()   # Logistic回归模型
    #     lr.fit(x, y.ravel())        # 根据数据[x,y]，计算回归参数
    #
    # 等价形式
    lr = Pipeline([('sc', StandardScaler()),
                        ('clf', LogisticRegression()) ])#lr默认为逻辑回归
    lr.fit(x, y.ravel())#numpy的ravel() 和 flatten()函数：
# 简介
#
# 首先声明两者所要实现的功能是一致的（将多维数组降位一维）。这点从两个单词的意也可以看出来，
# ravel(散开，解开)，flatten（变平）。两者的区别在于返回拷贝（copy）还是返回视图（view），numpy.flatten()返回一份拷贝，
# 对拷贝所做的修改不会影响（reflects）原始矩阵，
# 而numpy.ravel()返回的是视图（view，也颇有几分C/C++引用reference的意味），会影响（reflects）原始矩阵。

    # 画图
    N, M = 500, 500     # 横纵各采样多少个值
    x1_min, x1_max = x[:, 0].min(), x[:, 0].max()   # 第0列的范围
    x2_min, x2_max = x[:, 1].min(), x[:, 1].max()   # 第1列的范围
    t1 = np.linspace(x1_min, x1_max, N)
    t2 = np.linspace(x2_min, x2_max, M)
    x1, x2 = np.meshgrid(t1, t2)                    # 生成网格采样点
    x_test = np.stack((x1.flat, x2.flat), axis=1)   # 测试点

    # 无意义，只是为了凑另外两个维度
    # x3 = np.ones(x1.size) * np.average(x[:, 2])
    # x4 = np.ones(x1.size) * np.average(x[:, 3])
    # x_test = np.stack((x1.flat, x2.flat, x3, x4), axis=1)  # 测试点

    cm_light = mpl.colors.ListedColormap(['#77E0A0', '#FF8080', '#A0A0FF'])
    cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])
    y_hat = lr.predict(x_test)                  # 预测值
    y_hat = y_hat.reshape(x1.shape)                 # 使之与输入的形状相同
    plt.pcolormesh(x1, x2, y_hat, cmap=cm_light)     # 预测值的显示
    plt.scatter(x[:, 0], x[:, 1], c=y, edgecolors='k', s=50, cmap=cm_dark)    # 样本的显示
    plt.xlabel('petal length')
    plt.ylabel('petal width')
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.grid()
    plt.savefig('2.png')
    plt.show()

    # 训练集上的预测结果
    y_hat = lr.predict(x)
    y = y.reshape(-1)
    result = y_hat == y
    print (y_hat)
    print (result)
    acc = np.mean(result)
    print( '准确度: %.2f%%' % (100 * acc))
