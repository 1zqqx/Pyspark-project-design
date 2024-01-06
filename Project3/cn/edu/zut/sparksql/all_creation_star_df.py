# -*- coding: utf-8 -*-
# @Author  : x_DARK_
# @FileName: all_creation_star_df.py
# @Time    : 2024/1/6 0006 16:11
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
    df = spark.read.jdbc(url=url, table='all_creation_star', properties=properties)

    df.groupby(['book_first_partition', 'book_status']) \
        .count() \
        .sort(df.book_first_partition.desc(), df.book_status.asc()) \
        .show(1000)

    df.printSchema()

    spark.stop()
    pass


if __name__ == '__main__':
    _test()
