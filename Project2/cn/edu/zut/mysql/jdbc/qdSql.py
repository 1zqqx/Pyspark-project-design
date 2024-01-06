# -*- coding: utf-8 -*-
# @Author  : x_DARK_
# @FileName: qdSql.py
# @Time    : 2024/1/5 0005 20:50
# @Software: PyCharm

import json

import mysql.connector
from mysql.connector import Error


def _test():
    global conn, cursor
    try:
        conn = mysql.connector.connect(
            host="192.168.231.140",
            port=3306,
            user='liuqiqi',
            password='liuqiqi',
            database='pysql'
        )
        cursor = conn.cursor(prepared=True)

        json_path = ("F:/WorkSpace/Software Engineering Practice 2/Pyspark project "
                     "design/Project1/qdFiction/qdFiction/spiders/202001_202401_month_list.json")

        data_lt = []
        with open(json_path, 'r', encoding='utf8') as fs:
            for line in json.load(fs):
                data_lt.append((
                    line['book_name'], line['book_author'], line['book_first_partition'], line['book_second_partition'],
                    line['book_status'], line['book_intro'], line['date_list'] + '-1'
                ))
        sql = """
            INSERT INTO qd_yuepiao(id,book_name,book_author,book_first_partition, \
            book_second_partition,book_status,book_intro,date_list) \
            values(null,?,?,?,?,?,?,?)
        """

        cursor.executemany(sql, data_lt)
        conn.commit()
        print("[=] INFO OK")
    except Error as e:
        conn.rollback()
        print(f"[=] Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
    pass


if __name__ == '__main__':
    _test()
