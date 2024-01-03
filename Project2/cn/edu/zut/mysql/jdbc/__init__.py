# -*- coding: utf-8 -*-
# @Author  : x_DARK_
# @FileName: __init__.py
# @Time    : 2024/1/2 0002 09:06
# @Software: PyCharm

import pymysql


def main():
    # 打开数据库连接
    global db
    try:
        db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='pysql')
        print('connect approve')
    except:
        print('connect error')

    # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    # cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()
    # print("Database version : %s " % data)

    # cursor = db.cursor()
    # cursor.execute("DROP TABLE IF EXISTS pysql")
    #
    # sql = """
    #     CREATE TABLE IF NOT EXISTS students (
    #     FIRST_NAME  CHAR(20) NOT NULL,
    #     LAST_NAME  CHAR(20),
    #     AGE INT,
    #     SEX CHAR(1),
    #     INCOME FLOAT )"""
    #
    # cursor.execute(sql)
    # print("Table creation successful!")

    # cursor = db.cursor()
    # sql = """
    # INSERT INTO students
    #        (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    #        VALUES ('Mac', 'Mohan', 20, 'M', 2000)
    # """
    # try:
    #     # 执行sql语句
    #     cursor.execute(sql)
    #     # 提交数据库执行
    #     db.commit()
    #     print("insert successful!")
    # except:
    #     # 如果发生错误则回滚
    #     db.rollback()
    #     print("insert error")

    # cursor = db.cursor()
    # sql = """
    # SELECT * FROM students
    # WHERE INCOME > 1999
    # """
    # try:
    #     cursor.execute(sql)
    #     results = cursor.fetchall()
    #     for row in results:
    #         fname = row[0]
    #         lname = row[1]
    #         age = row[2]
    #         sex = row[3]
    #         income = row[4]
    #         print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" %
    #               (fname, lname, age, sex, income))
    # except:
    #     print("Error: unable to fetch data")

    # 将表中 SEX 为 'M' 的 AGE 字段递增 1
    # cursor = db.cursor()
    # sql = "UPDATE students SET AGE = AGE + 1 WHERE SEX = '%c'" % 'M'
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    #     print("update successful!")
    # except:
    #     db.rollback()
    #     print("update error")

    # cursor = db.cursor()
    # sql = "DELETE FROM students WHERE AGE > %s" % 20
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    #     print('delete approve')
    # except:
    #     db.rollback()
    #     print('delete error')
    db.close()
    pass


if __name__ == '__main__':
    main()
