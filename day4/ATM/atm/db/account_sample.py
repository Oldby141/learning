#!_*_coding:utf-8_*_

import json
acc_dic = {
    "id":1234,
    'password':'abc',
    'credit':15000,
    'balance':15000,
    'enroll_data':'2016-01-02',
    'expire_data':'2011-01-02',
    'pay_day':22,
    'status':0#  0 = nomal , 1 = locked , 2 = disabled
}

print(json.dumps(acc_dic))