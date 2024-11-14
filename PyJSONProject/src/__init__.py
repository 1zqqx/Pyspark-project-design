# -*- coding: utf-8 -*-
# @Author  : x_DARK_
# @FileName: __init__.py.py
# @Time    : 2024/11/14 0014 15:58
# @Software: PyCharm


import json
import pandas as pd

data = pd.read_csv('F:\WorkSpace\Software Engineering Practice 2\Pyspark project design\PyJSONProject\data\json.csv')

# 重新设置列名
data.columns = ['action', 'event_type', 'customer_id', 'device_num', 'device_type', 'os', 'os_version', 'manufacturer',
                'carrier', 'network_type', 'area_code', 'longitude', 'latitude', 'extinfo', 'target_type',
                'target_keys', 'target_order', 'target_ids', 'target_action', 'target_id', 'ct']

data['data'] = data.apply(lambda row: json.dumps({
    'action': row['action'],
    'event_type': row['event_type'],
    'customer_id': row['customer_id'],
    'device_num': row['device_num'],
    'device_type': row['device_type'],
    'os': row['os'],
    'os_version': row['os_version'],
    'manufacturer': row['manufacturer'],
    'carrier': row['carrier'],
    'network_type': row['network_type'],
    'area_code': row['area_code'],
    'longitude': row['longitude'],
    'latitude': row['latitude'],
    'extinfo': row['extinfo'],
    'target_type': row['target_type'],
    'target_keys': row['target_keys'],
    'target_order': row['target_order'],
    'target_ids': row['target_ids'],
    'target_action': row['target_action'],
    'target_id': row['target_id'],
    'ct': row['ct']
}), axis=1)


# 删除action、event_type、customer_id、device_num、device_type、os、os_version、manufacturer、carrier、network_type、area_code、longitude、latitude、extinfo、target_type、target_keys、target_order、target_ids、target_action、target_id、ct列
data = data.drop(['action', 'event_type', 'customer_id', 'device_num', 'device_type', 'os', 'os_version', 'manufacturer', 'carrier', 'network_type', 'area_code', 'longitude', 'latitude', 'extinfo', 'target_type', 'target_keys', 'target_order', 'target_ids', 'target_action', 'target_id', 'ct'], axis=1)

# 将data列的数据转换为JSON格式
data['data'] = data['data'].apply(json.loads)

# 将data列的数据转换为DataFrame格式
data = data['data'].apply(pd.Series)

print("数据的前几行:")
print(data['action'])