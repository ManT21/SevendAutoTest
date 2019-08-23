#!/usr/bin/env python
# coding=utf-8
import pymysql


def connectdb():
    # 打开数据库连接
    # 用户名:hp, 密码:Hp12345.,用户名和密码需要改成你自己的mysql用户名和密码，并且要创建数据库TESTDB，并在TESTDB数据库中创建好表Student
    try:
        db = pymysql.connect(host='10.40.11.180', user='root', password='dafy1024', port=3306)
        return db
    except:
        print("连接失败")


def fetchonedb(sql):
    db = connectdb()

    # 使用cursor()方法获取操作游标
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # SQL 查询语句
    sql = sql
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        result = cursor.fetchone()
        return result
    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    db.close()


def updatedb(sql):
    db = connectdb()

    # 使用cursor()方法获取操作游标
    cursor = db.cursor(pymysql.cursors.DictCursor)

    # SQL 查询语句
    sql = sql
    #try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    db.commit()
    #except:
    #    print("Error: unable to update data")
    # 关闭数据库连接
    cursor.close()
    db.close()

