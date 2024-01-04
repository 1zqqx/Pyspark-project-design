# -*- coding: utf-8 -*-
# @Author  : x_DARK_
# @FileName: __init__.py.py
# @Time    : 2024/1/4 0004 08:39
# @Software: PyCharm

from pyspark import SparkContext, SparkConf

conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("App") \
    .set("spark.driver.bindAddress", "127.0.0.1") \
    .set("spark.executor.memory", "2g")

sc = SparkContext(conf=conf)

print(sc.version)

sc.stop()

if __name__ == '__main__':
    pass
