# -*- coding: utf-8 -*-
# @Author  : x_DARK_
# @FileName: pyRdd.py
# @Time    : 2024/1/4 0004 10:08
# @Software: PyCharm

import random
import os
from pyspark import SparkContext, SparkConf

os.environ['PYSPARK_PYTHON'] = "E:/Python/python.exe"

conf = SparkConf() \
    .setMaster("local[2]") \
    .setAppName("App") \
    .set("spark.driver.bindAddress", "127.0.0.1")

sc = SparkContext(conf=conf)


# rdd1 = sc.parallelize([random.randint(1, 1000) for i in range(10)])
# print(rdd1.collect())
# rdd2 = sc.textFile("dt.txt")
# print(rdd2.collect())

def func(d):
    if d & 1:
        return d


rdd3 = sc.parallelize([random.randint(1, 1000) for i in range(10)])
print(rdd3.collect())
rdd3 = rdd3.map(func)
print(rdd3.collect())

sc.stop()


def _test():
    pass


if __name__ == '__main__':
    _test()
