import redisdb
import mysql
import requests
from commonfunction import *
from readconfig import *


def get_loan_support_type(mobile):
    interface_url = read_interface_config("GET_SUPPORT_LOAN_TYPE")
    pwd = read_password_config(mobile)
    session_key = get_session_key_by_mobile_or_login(mobile, pwd)
    data = {'session_key': session_key}
    r = requests.post(interface_url, data=data)
    result = r.json()
    return result


result = get_loan_support_type('13400000039')
print(result)
#def build_repay_plan(mobile, monney, )