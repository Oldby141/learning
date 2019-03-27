#!_*_coding:utf-8_*_
import time
from core import db_handler


def login_required(func):

    def wrapper(*args,**kwargs):
        if args[0].get('is_authenticated'):
            return func(*args,**kwargs)
        else:
            exit("User is not authenticated.")
    return wrapper

def acc_auth2(account,password):
    db_api = db_handler.db_handler()
    data = db_api('select * from accounts where account=%s'%account)
    #print(data)

    if data['password'] == password:
        exp_time_stamp = time.mktime(time.strptime(data['expire_date'],"%Y-%m-%d"))
        if time.time() >exp_time_stamp:
            print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m"%account)
        else:
            return data
    else:
        print("\033[31;1mAccount ID or password is incorrect!\033[0m")

def acc_login(user_data,log_obj):
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth = acc_auth2(account,password)
        if auth:
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            return auth
        retry_count+=1
    else:
        log_obj.error("account [%s] too many login attempts" %account)
        exit()