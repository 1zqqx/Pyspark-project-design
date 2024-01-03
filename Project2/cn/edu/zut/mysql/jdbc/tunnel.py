# -*- coding: utf-8 -*-
# @Author  : x_DARK_
# @FileName: tunnel.py
# @Time    : 2024/1/3 0003 09:51
# @Software: PyCharm

import json

import mysql.connector
from mysql.connector import Error


def main():
    global conn, cursor
    try:
        conn = mysql.connector.connect(
            host="192.168.231.140",
            port='3306',
            user='liuqiqi',
            password='liuqiqi',
            database='pysql'
        )
        cursor = conn.cursor(prepared=True)

        json_path = "F:\\WorkSpace\\Software Engineering Practice 2\\Pyspark project design\\Project1\\ljxSpider\\ljxSpider\\spiders\\a.json"
        with open(json_path, 'r', encoding='utf8') as fs:
            data_all = json.load(fs)

        sql = ("INSERT INTO doubantop250(id,movies_img,movies_name,movies_name_en,movies_other_name,movies_director,\
            movies_lead_role,movies_time,movies_sector,movies_score,movies_eva_number,movies_sign) \
            values(0,?,?,?,?,?,?,?,?,?,?,?)")

        data = []
        for i in data_all:
            data.append((
                i['moviesImg'], i['moviesName'], i['moviesNameEn'], i['moviesOtherName'],
                i['moviesDirector'],
                i['moviesLeadRole'], i['moviesTime'], str(i['moviesSector']),
                i['moviesScore'], int(i['moviesEvaNumber']), i['moviesSign'])
            )
        # print(type(data))
        cursor.executemany(sql, data)
        conn.commit()
    except Error as error:
        conn.rollback()  # 执行失败，数据回滚
        print(f"{error}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
    pass


if __name__ == '__main__':
    main()
