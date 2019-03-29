#!_*_coding:utf-8_*_

import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
import matplotlib as mpl
import matplotlib.pyplot as plt

def iris_type(s):
    it = {b'Iris-setosa': 0, b'Iris-versicolor': 1, b'Iris-virginica': 2}
    return it[s]

iris_feature = u'花萼长度', u'花萼宽度', u'花瓣长度', u'花瓣宽度'

def show_accuracy(a,b,tip):
    acc = a.ravel() == b.ravel()
    print(tip + '正确率:',np.mean(acc))

if __name__ == "__main__":
    path = '..\\09决策树\\8.iris.data'
    data = np.loadtxt(path,dtype=float,delimiter=',',converters={4:iris_type})
    x,y = np.split(data,(4,),axis=1)
    x = x[:,:2]
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=0.6)

    #分类器
    #clf = svm.SVC(C = 0.1,kernel='linear', decision_function_shape='ovr')
    clf = svm.SVC(C=0.8,kernel='rbf',gamma=20,decision_function_shape='ovr')#decision_function_shape=ovr指分三个列，每个类别的可能取值
    clf.fit(x_train,y_train.ravel())

    #准确率
    print(clf.score(x_train,y_train))
    y_hat = clf.predict(x_train)
    show_accuracy(y_hat,y_train,'训练集')
    print(clf.score(x_test,y_test))
    y_hat = clf.predict(x_test)
    show_accuracy(y_hat,y_test,'测试集')

    #画图
    x1_min,x1_max = x[:,0].min(),x[:,0].max()#第0列的范围
    x2_min,x2_max = x[:,1].min(),x[:,1].max()#第1列的范围
    x1,x2 = np.mgrid[x1_min:x1_max:500j,x2_min:x2_max:500j]#生成网格采样点
    grid_test = np.stack((x1.flat,x2.flat),axis=1)

    Z = clf.decision_function(grid_test)
    print(Z)
    grid_hat = clf.predict(grid_test)
    print(grid_hat)
    grid_hat = grid_hat.reshape(x1.shape)  # 使之与输入的形状相同
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])#区域的颜色
    cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])#点的颜色
    x1_min, x1_max = x[:, 0].min(), x[:, 0].max()  # 第0列的范围
    x2_min, x2_max = x[:, 1].min(), x[:, 1].max()  # 第1列的范围
    x1, x2 = np.mgrid[x1_min:x1_max:500j, x2_min:x2_max:500j]  # 生成网格采样点
    grid_test = np.stack((x1.flat, x2.flat), axis=1)  # 测试点
    plt.pcolormesh(x1, x2, grid_hat, cmap=cm_light)# 预测值的显示

    plt.scatter(x[:, 0], x[:, 1], c=y, edgecolors='k', s=50, cmap=cm_dark)      # 样本
    plt.scatter(x_test[:, 0], x_test[:, 1], s=120, facecolors='none', zorder=10)     # 圈中测试集样本
    plt.xlabel(iris_feature[0], fontsize=13)
    plt.ylabel(iris_feature[1], fontsize=13)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.title(u'鸢尾花SVM二特征分类', fontsize=15)
    plt.grid()
    plt.show()
