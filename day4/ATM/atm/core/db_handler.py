#!_*_coding:utf-8_*_
from conf import settings
import json,time,os

def file_db_handle(conn_params):
    #print('file_db:',conn_params)
    return file_execute

def db_handler():
    conn_params = settings.DATABASE
    if conn_params['engine'] == 'file_storage':
        return file_db_handle(conn_params)
    elif conn_params['engine'] == 'mysql':
        pass

def file_execute(sql,**kwargs):
    conn_params = settings.DATABASE
    db_path = '%s/%s'%(conn_params['path'],conn_params['name'])

    #print(sql,db_path)
    sql_list = sql.split("where")
    #print(sql_list)
    if sql_list[0].startswith("select") and len(sql_list)>1:
        column,val = sql_list[1].strip().split('=')
        #print(val)

        if column == 'account':
            account_file = '%s/%s.json'%(db_path,val)
            #print(account_file)
            #print(os.path.isfile(account_file))
            if os.path.isfile(account_file):
                with open(account_file,"r") as f:
                    account_data = json.load(f)
                    return account_data
            else:
                exit("\033[31;1mAccount [%s] does not exist!\033[0m" % val)

    elif sql_list[0].startswith("update") and len(sql_list) > 1:  # has where clause
        column, val = sql_list[1].strip().split("=")
        if column == 'account':
            account_file = "%s/%s.json" % (db_path, val)
            # print(account_file)
            if os.path.isfile(account_file):
                account_data = kwargs.get("account_data")
                with open(account_file, 'w') as f:
                    acc_data = json.dump(account_data, f)
                return True
