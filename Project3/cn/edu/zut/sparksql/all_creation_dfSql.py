# -*- coding: utf-8 -*-
# @Author  : x_DARK_
# @FileName: all_creation_dfSql.py
# @Time    : 2024/1/6 0006 13:49
# @Software: PyCharm

from pyspark.sql import SparkSession


def _test():
    spark = SparkSession \
        .builder \
        .appName("all_creation_dfSql") \
        .master("local[2]") \
        .config("spark.driver.bindAddress", "127.0.0.1") \
        .getOrCreate()

    # 解决乱码问题
    url = "jdbc:mysql://192.168.231.140:3306/pysql?characterEncoding=utf8"
    properties = {
        'user': 'liuqiqi', 'password': 'liuqiqi', 'driver': 'com.mysql.jdbc.Driver'
    }
    df = spark.read.jdbc(url=url, table='all_creation', properties=properties)

    df.groupby(['book_first_partition', df.book_second_partition, df.book_status]) \
        .count() \
        .sort(df.book_first_partition.desc(), df.book_second_partition.desc(), df.book_status.desc()) \
        .write.jdbc(
        url=url, table='all_creation_dfsql', mode='overwrite', properties=properties)

    # print(">+<" * 30)

    df.groupby("book_author") \
        .agg({"book_author": "count"}) \
        .withColumnRenamed("count(book_author)", "count") \
        .orderBy("count", ascending=False) \
        .write.jdbc(
        url=url, table='all_creation_dfsql_author', mode='overwrite', properties=properties)

    # print(type(df))
    # print(df.schema)
    df.printSchema()

    spark.stop()
    pass


if __name__ == '__main__':
    _test()
