# -*- coding:utf-8 -*-

import numpy as np
from sklearn.linear_model import LinearRegression, RidgeCV,LassoCV,ElasticNetCV
from sklearn.preprocessing import PolynomialFeatures#进行特征的构造
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
import matplotlib as mpl
from sklearn.exceptions import  ConvergenceWarning
import warnings

if __name__ == "__main__":

    warnings.filterwarnings(action='ignore', category=ConvergenceWarning)
    np.random.seed(0)#当我们设置相同的seed，每次生成的随机数相同
    N = 9#9个点
    x = np.linspace(0, 6, N) + np.random.randn(N)#rand函数根据给定维度生成[0,1)之间的数据，包含0，不包含1  randn函数返回一个或一组样本，具有标准正态分布。
    x = np.sort(x)
    y = x**2 - 4*x - 3 + np.random.randn(N)
    x.shape = -1, 1 #代表一列，-1代表自动对齐
    y.shape = -1, 1

    model_1 = Pipeline([
        ('poly', PolynomialFeatures()),
        ('linear', LinearRegression(fit_intercept=False))])#fit_intercept:是否有截据，如果没有则直线过原点。normalize:是否将数据归一化。
    model_2 = Pipeline([
        ('poly', PolynomialFeatures()),
        ('linear', RidgeCV(alphas=np.logspace(-3, 2, 100), fit_intercept=False))])
    model_3 = Pipeline([
        ('poly', PolynomialFeatures()),
        ('linear', LassoCV(alphas=np.logspace(-3, 2, 100), fit_intercept=False))])
    # model_4 = Pipeline([
    #     ('Poly', PolynomialFeatures()),
    #     ('Linear', ElasticNetCV(alphas=np.logspace(-3, 2, 50), l1_ratio=[.1, .5, .7, .9, .95, 1], fit_intercept=False))
    # ])
    models = model_1, model_2,model_3#,model_4
    mpl.rcParams['font.sans-serif'] = [u'simHei']#修改字体为黑体，但负号将无法显示
    mpl.rcParams['axes.unicode_minus'] = False#添加后可显示负号
    np.set_printoptions(suppress=True)#suppress消除小的数字使用科学记数法  解决python中 ndarray 默认用科学计数法显示的问题

    plt.figure(figsize=(6 , 10), facecolor='w')
    d_pool = np.arange(1, N, 1)  # 阶
    m = d_pool.size
    clrs = []  # 颜色
    for c in np.linspace(16711680, 255, m):#16711680代表红色，255代表蓝色
        clrs.append('#%06x' % int(c))
    line_width = np.linspace(5, 2, m)
    titles = u'线性回归', u'Ridge回归' ,u"Lasso回归",u'ElasticNet'
    for t in range(3):
        model = models[t]
        plt.subplot(3, 1, t+1)#t+1表示位置
        plt.plot(x, y, 'ro', ms=5, zorder=N)
        for i, d in enumerate(d_pool):
            model.set_params(poly__degree=d)#调用时加__再加属性
            model.fit(x, y)
            lin = model.get_params('linear')['linear']
            if t == 0:
                print (u'%d阶，系数为：' % d, lin.coef_.ravel())
            else:
                print (u'%d阶，alpha=%.6f，系数为：' % (d, lin.alpha_), lin.coef_.ravel())
            x_hat = np.linspace(x.min(), x.max(), num=100)
            x_hat.shape = -1, 1
            y_hat = model.predict(x_hat)
            s = model.score(x, y)
            print (s, '\n')
            zorder = N - 1 if (d == 2) else 0
            plt.plot(x_hat, y_hat, color=clrs[i], linewidth=2, label=(u'%d阶，score=%.3f' % (d, s)), zorder=zorder)
        plt.legend(loc='upper left')
        plt.grid(True)
        plt.title(titles[t], fontsize=16)
        plt.xlabel('X', fontsize=14)
        plt.ylabel('Y', fontsize=14)
    plt.tight_layout(1, rect=(0, 0, 1, 0.95))#tight_layout会自动调整子图参数，使之填充整个图像区域
    plt.suptitle(u'多项式曲线拟合', fontsize=18)
    plt.show()
