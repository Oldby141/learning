# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import GridSearchCV


if __name__ == "__main__":
    # pandas读入
    data = pd.read_csv('8.Advertising.csv')    # TV、Radio、Newspaper、Sales
    x = data[['TV', 'Radio', 'Newspaper']]
    # x = data[['TV', 'Radio']]
    y = data['Sales']


    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
    # print x_train, y_train
    model = Lasso()
    # model = Ridge()

    alpha_can = np.logspace(-3, 2, 10)#alpha参数集 10^-3~10^2的等比数列的10个数
    lasso_model = GridSearchCV(model, param_grid={'alpha': alpha_can}, cv=5)#其中cv可以是整数或者交叉验证生成器或一个可迭代器，cv参数对应4种输入：
# 1、None:默认参数，哈数会使用默认的3折交叉验证
# 2、整数k：K折交叉验证。对于分类任务，使用stratifiedFold(类别平衡，每类的训练集占比一样多），对于其他任务，使用Kfold
# 3、交叉验证生成器：得自己写生成器，头疼，略
# 4、可以生成训练集与测试集的迭代器：同上，略

    lasso_model.fit(x, y)
    print ('验证参数：\n', lasso_model.best_params_)

    y_hat = lasso_model.predict(np.array(x_test))
    mse = np.average((y_hat - np.array(y_test)) ** 2)  # Mean Squared Error
    rmse = np.sqrt(mse)  # Root Mean Squared Error
    print (mse, rmse)

    t = np.arange(len(x_test))
    plt.plot(t, y_test, 'r-', linewidth=2, label='Test')
    plt.plot(t, y_hat, 'g-', linewidth=2, label='Predict')
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()
