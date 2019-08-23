import redisdb
import mysql
import rsamethod
import requests
from readconfig import read_interface_config


def get_customer_id_by_mobile(mobile):
    sql = "SELECT id FROM sevend.t_customer WHERE mobile = %s and state = 1;" % mobile
    try:
        res = mysql.fetchonedb(sql)
        customer_id = res['id']
        return customer_id
    except:
        print("this mobile doesn't exist")


def get_session_key_by_mobile(mobile):
    try:
        customer_id = get_customer_id_by_mobile(mobile)
        session_key = bytes.decode(redisdb.get_key('session_' + str(customer_id)))
        return session_key
    except:
        print("this mobile doesn't online")


def login_by_password(mobile, password):
    try:
        redisdb.del_key('login_pwd_limit_'+mobile)
        interface_url = read_interface_config("LOAN")
        pwd = rsamethod.rsaEncrypt(password)
        account = {'mobile': mobile, 'pwd': pwd}
        r = requests.post(interface_url, data=account)
        result = r.json()
        return result
    except:
        print("login failed")


def get_session_key_by_mobile_or_login(mobile, password):
    try:
        customer_id = get_customer_id_by_mobile(mobile)
        session_key = bytes.decode(redisdb.get_key('session_' + str(customer_id)))
        return session_key
    except:
        login_by_password(mobile, password)
        customer_id = get_customer_id_by_mobile(mobile)
        session_key = bytes.decode(redisdb.get_key('session_' + str(customer_id)))
        return session_key


