#!_*_coding:utf-8_*_
import json
import time
from core import db_handler
from conf import settings

def load_current_balance(account_id):
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s"%account_id)
    #print(data)
    return data

def dump_account(account_data):
    db_api = db_handler.db_handler()
    data = db_api("update accounts where account=%s" % account_data['id'],account_data=account_data)
    return True