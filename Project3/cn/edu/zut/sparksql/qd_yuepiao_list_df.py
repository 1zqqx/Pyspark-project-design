# -*- coding: utf-8 -*-
# @Author  : x_DARK_
# @FileName: qd_yuepiao_list_df.py
# @Time    : 2024/1/6 0006 16:30
# @Software: PyCharm
from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import *


def _test():
    spark = SparkSession \
        .builder \
        .appName("all_creation_star_df") \
        .master("local[2]") \
        .config("spark.driver.bindAddress", "127.0.0.1") \
        .getOrCreate()

    url = "jdbc:mysql://192.168.231.140:3306/pysql?characterEncoding=utf8"
    properties = {
        'user': 'liuqiqi', 'password': 'liuqiqi', 'driver': 'com.mysql.jdbc.Driver'
    }
    df = spark.read.jdbc(url=url, table='qd_yuepiao', properties=properties)

    # 词云图 二级分区 数据格式data = [("生活资源", "999"),("供热管理", "888"),("供气质量", "777")]
    # df.groupBy("book_second_partition") \
    #     .agg({"book_second_partition": "count"}) \
    #     .withColumnRenamed("count(book_second_partition)", "count") \
    #     .orderBy("count", ascending=False) \
    #     .write.jdbc(
    #     url=url, table="qd_yuepiao_cloud_part_list", mode="overwrite", properties=properties)
    # df.groupBy("book_first_partition") \
    #     .agg({"book_first_partition": "count"}) \
    #     .withColumnRenamed("count(book_first_partition)", "count") \
    #     .orderBy("count", ascending=False) \
    #     .write.jdbc(
    #     url=url, table="qd_yuepiao_cloud_f_part_list", mode="overwrite", properties=properties)

    # qd top25 作者 书 数
    # df.groupBy("book_author") \
    #     .agg(sf.count(df["book_author"]).alias("count")) \
    #     .orderBy("count", ascending=False) \
    #     .write.jdbc(
    #     url=url, table="qd_yuepiao_author_count", mode="overwrite", properties=properties)

    # 月份 榜 一级分区
    _df1 = df.groupBy(["date_list", "book_first_partition"]) \
        .agg(count("book_first_partition").alias("count"))
    # print(type(_df1))
    # 创建窗口规范，按照班级进行分组，并按照分数降序排序
    windowSpec = Window.partitionBy("date_list").orderBy(col("count").desc())
    # 使用row_number()函数为每个分组的每一行分配一个排名
    df_with_rank = _df1.withColumn("Rank", row_number().over(windowSpec))
    # 过滤排名小于等于5的行
    df_top_n = df_with_rank.filter(col("Rank") <= 5)
    # df_top_n.show()
    df_top_n.write.jdbc(
        url=url, table="qd_yuepiao_date_top_count", mode="overwrite", properties=properties)

    df.printSchema()
    spark.stop()
    pass


if __name__ == '__main__':
    _test()
