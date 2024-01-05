# -*- coding: utf-8 -*-
# @Author  : x_DARK_
# @FileName: pyRdd.py
# @Time    : 2024/1/4 0004 10:08
# @Software: PyCharm

import random
import os
import re
import string

from pyspark import SparkContext, SparkConf

os.environ['PYSPARK_PYTHON'] = "E:/Python/python.exe"

conf = SparkConf() \
    .setMaster("local[2]") \
    .setAppName("App") \
    .set("spark.driver.bindAddress", "127.0.0.1") \
    .set("spark.executor.memory", "2g")

sc = SparkContext(conf=conf)


# rdd1 = sc.parallelize([random.randint(1, 1000) for i in range(10)])
# print(rdd1.collect())
# rdd2 = sc.textFile("dt.txt")
# print(rdd2.collect())

# def func(d):
#     if d & 1:
#         return d


# rdd3 = sc.parallelize([random.randint(1, 1000) for i in range(10)])
# print(rdd3.collect())
# rdd3 = rdd3.map(func)
# print(rdd3.collect())
# rdd3.map(lambda x: x + 2).filter(lambda x: x > 500).foreach(print)

# data = ["1, 2, 1", "1, 2, 2", "3, 2, 1"]
# rdd4 = sc.parallelize(data)
# rdd4 = rdd4.flatMap(lambda x: x.split(', ')) \
#     .map(lambda x: (x, 1)) \
#     .countByKey()
# print(rdd4)

# data = ["1, 2, 1", "1, 2, 2", "3, 2, 1"]
# rdd5 = sc.parallelize(data)
# rdd5 = rdd5.flatMap(lambda x: x.split(', ')) \
#     .map(lambda x: (x, 1)) \
#     .reduceByKey(lambda x, y: y + y) \
#     .collect()
# print(rdd5)

# 转小写 & 去掉非字母字符
def func(s: string):
    s = s.lower()
    return re.findall('[a-zA-Z]+', s)[0]
    pass


rdd6 = sc.textFile("dt.txt")
rdd6.flatMap(lambda x: x.split(' ')) \
    .map(lambda x: func(x)) \
    .map(lambda x: (x, 1)) \
    .reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda x: x[1], ascending=False, numPartitions=4) \
    .foreach(print)

# .filter(lambda x: re.match(r'^[a-zA-Z]+$', x) is not None) \
# print(rdd6.collect())

sc.stop()


def _test():
    pass


if __name__ == '__main__':
    _test()
