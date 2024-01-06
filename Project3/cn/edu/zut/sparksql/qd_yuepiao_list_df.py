# -*- coding: utf-8 -*-
# @Author  : x_DARK_
# @FileName: qd_yuepiao_list_df.py
# @Time    : 2024/1/6 0006 16:30
# @Software: PyCharm
from pyspark.sql import SparkSession


def _test():
    spark = SparkSession \
        .builder \
        .appName("all_creation_star_df") \
        .master("local[2]") \
        .config("spark.driver.bindAddress", "127.0.0.1") \
        .getOrCreate()

    url = "jdbc:mysql://192.168.231.140:3306/pysql"
    properties = {
        'user': 'liuqiqi', 'password': 'liuqiqi', 'driver': 'com.mysql.jdbc.Driver'
    }
    df = spark.read.jdbc(url=url, table='qd_yuepiao', properties=properties)

    df.show()
    df.printSchema()

    spark.stop()
    pass


if __name__ == '__main__':
    _test()
