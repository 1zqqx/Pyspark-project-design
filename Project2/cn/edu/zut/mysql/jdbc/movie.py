# -*- coding: utf-8 -*-
# @Author  : x_DARK_
# @FileName: movie.py
# @Time    : 2024/1/3 0003 09:12
# @Software: PyCharm

import mysql.connector


def main():
    conn = mysql.connector.connect(
        host='192.168.231.140',
        port='3306',
        user='liuqiqi',
        password='liuqiqi',
        database='pysql'
    )

    cursor = conn.cursor()

    cursor.execute("select * from douban")

    results = cursor.fetchall()

    for i in results:
        dt = {'id': i[0], 'movieName': i[1], 'movieDirector': i[2]}
        print(dt)

    cursor.close()
    conn.close()
    pass


if __name__ == '__main__':
    main()
