# -*- coding: utf-8 -*-
# @Author  : x_DARK_
# @FileName: odps2mysql.py
# @Time    : 2024/11/14 0014 17:22
# @Software: PyCharm


# 这个脚本可以读取你的 MaxCompute 中，指定项目中的所有的表，以及表的结构。并且自动完成支持 MySQL 的建表语句。
# 在执行的时候，需要有第三方的依赖。 pip install pyodps

from odps import ODPS

# 设置项目的基础属性配置
access_id = '{换成自己的ACCESS_ID}'
access_key = '{换成自己的ACCESS_KEY}'
project = 'aliyun_bigdata_0000'
endpoint = 'https://service.cn-shenzhen.maxcompute.aliyun.com/api'
mysql_dbname = 'ads_nshop_0000'


def type_adapter(maxcompute_type: str):
    """
    将 MaxCompute 中的数据类型转换成为MySQL支持的数据类型
    :param maxcompute_type: MaxCompute中的数据类型
    :return: MySQL中支持的数据类型
    """
    if maxcompute_type.lower() == 'string':
        return 'varchar(128)'

    if maxcompute_type.lower() == 'int' or maxcompute_type.lower() == 'bigint' or maxcompute_type.lower() == 'tinyint':
        return 'int'

    if maxcompute_type.lower().startswith('decimal') or maxcompute_type.lower().startswith(
            'float') or maxcompute_type.lower().startswith('double'):
        return 'double'


# 获取 MaxCompute 连接对象
odps_obj = ODPS(access_id, access_key, project, endpoint)

# 获取到指定的表
for table_obj in odps_obj.list_tables(prefix='ads'):
    # 准备字符串，用来拼接 MySQL 的建表语句
    sql: str = f'create table if not exists {mysql_dbname}.{table_obj.name} (\n'
    # 获取到表中所有的字段信息
    for column in table_obj.table_schema.columns:
        # 将字段的名称、类型、备注拼接到建表语句SQL中
        sql += f"\t{column.name} {type_adapter(str(column.type))} comment '{column.comment}',\n"
    # 截取掉最后一个逗号
    sql = sql[:-2] + '\n);'

    print(sql)
