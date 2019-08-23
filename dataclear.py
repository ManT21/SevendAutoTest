import redisdb
import mysql
import commonfunction

def account_data_clear(mobile):
    customer_id = commonfunction.get_customer_id_by_mobile(mobile)
    fp = open("loandatahandlesql")
    sqls = fp.readlines()
    for sql in sqls:
        mysql.updatedb(eval(sql))


account_data_clear(13400000179)
