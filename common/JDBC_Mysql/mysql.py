#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql

def fileDB():
        batch_size = 5
        # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
        coon = pymysql.connect("10.32.189.250", "clm", "clm", "clm")
        # 使用 cursor() 方法创建一个游标对象 cursor
        # 使用cursor()方法获取操作游标
        cursor = coon.cursor()

        # 使用execute方法执行SQL语句
        sql = "SELECT * from t_attendance_record limit 10;"
        cursor.execute(sql)

        # 使用 fetchone() 方法获取一条数据
        txId = str(cursor.fetchall())
        print ("txId : %s " %txId )
        # 关闭数据库连接
        coon.close()
        # return txId[0]
