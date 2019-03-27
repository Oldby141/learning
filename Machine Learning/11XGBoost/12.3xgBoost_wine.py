#!_*_coding:utf-8_*_
import xgboost as xgb
import scipy.sparse
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

def read_data(path):#对毒蘑菇数据集的手写处理
    y = []
    row = []
    col = []
    values = []
    r = 0
    for d in open(path):
        d = d.strip().split()#以空格分开
        y.append(int(d[0]))
        d = d[1:]
        for c in d:
            key,value = c.split(':')
            row.append(r)
            col.append(int(key))
            values.append(float(value))
        r += 1
    x = scipy.sparse.csr_matrix((values,(row,col))).toarray()
    y = np.array(y)
    return x,y
def show_accuracy(a,b,tip):
    acc = a.ravel() == b.ravel()
    print(acc)
    print(tip + '正确率：\t',float(acc.sum())/a.size)

if __name__ =='__main__':
    # data = np.loadtxt('12.wine.data',dtype=float,delimiter=',')
    # y,x = np.split(data,(1,),axis=1)
    x,y =read_data('12.agaricus_train.txt')#
    #x = StandardScaler().fit_transform(x)
    x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1,test_size=0.5)

    #Logistic回归
    lr = LogisticRegression(penalty='l2')
    lr.fit(x_train,y_train.ravel())
    y_hat = lr.predict(x_test)
    show_accuracy(y_hat,y_test,'Logistic回归')

    #XGBoost
    y_train[y_train == 3] = 0#xgboost要求类别从0开始
    y_test[y_test == 3] = 0
    data_train = xgb.DMatrix(x_train,label=y_train)
    data_test = xgb.DMatrix(x_test,label=y_test)
    watch_list = [(data_test,'eval'),(data_train,'train')]
    param = {'max_depth':3,'eta':1,'silent':0,'objective':'multi:softmax','num_class':3}#softmax多分类不需要改为多列如001，123就可以
    bst = xgb.train(param, data_train, num_boost_round=4, evals=watch_list)
    y_hat = bst.predict(data_test)
    show_accuracy(y_hat,y_test,'XGBoost')