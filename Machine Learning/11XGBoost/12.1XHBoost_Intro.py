#!_*_coding:utf-8_*_
import xgboost as xgb
import numpy as np

#1,xgBoost的基本使用
#2，自定义损失函数的梯度和二阶导
#3,binary:logistic/logitraw

#定义f:theta * x
def log_reg(y_hat,y):
    p = 1.0/(1.0 + np.exp(-y_hat))
    g = p - y.get_label()
    h = p * (1.0 - p)
    return g,h

def error_rate(y_hat,y):
    return 'error',float(sum(y.get_label() != (y_hat > 0.5)))/len(y_hat)

if __name__ == "__main__":
    data_train = xgb.DMatrix('12.agaricus_train.txt')#处理稀疏矩阵
    data_test = xgb.DMatrix('12.agaricus_test.txt')

    param = {'max_depth':3,'eta':1,'silent':1,'objective':'binary:logitraw'}#eta 学习率 silent是否输出过程中的参数0代表输出
    #param = {'max_depth': 3, 'eta': 0.3, 'silent': 1, 'objective': 'reg:logistic'}
    watchlist = [(data_test,'eval'),(data_train,'train')]
    n_round = 3#训练的次数  即树的个数
    bst = xgb.train(param,data_train,num_boost_round=n_round,evals=watchlist)
    #bst = xgb.train(param, data_train, num_boost_round=n_round, evals=watchlist, obj=log_reg, feval=error_rate)

    #计算错误率
    y_hat = bst.predict(data_test)
    y = data_test.get_label()
    print(y_hat)
    print(y)
    error = sum(y!=(y_hat > 0.5))
    error_rate = float(error)/len(y_hat)
    print('样本总数：、t',len(y_hat))
    print('错误数目：\t%4d'%error)
    print('错误率:\t%.5f'%(100*error_rate))
# 另：参数解释
#     params = {
#         'booster': 'gbtree',
#         # 这里手写数字是0-9，是一个多类的问题，因此采用了multisoft多分类器，
#         'objective': 'multi:softmax',
#         'num_class': 10,  # 类数，与 multisoftmax 并用
#         'gamma': 0.05,  # 在树的叶子节点下一个分区的最小损失，越大算法模型越保守 。[0:]
#         'max_depth': 12,  # 构建树的深度 [1:]
#         # 'lambda':450,  # L2 正则项权重
#         'subsample': 0.4,  # 采样训练数据，设置为0.5，随机选择一般的数据实例 (0:1]
#         'colsample_bytree': 0.7,  # 构建树树时的采样比率 (0:1]
#         # 'min_child_weight':12, # 节点的最少特征数
#         'silent': 1,
#         'eta': 0.005,  # 如同学习率
#         'seed': 710,
#         'nthread': 4,  # cpu 线程数,根据自己U的个数适当调整
#     }