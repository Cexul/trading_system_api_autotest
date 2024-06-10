# coding:utf-8

import json
"""
    字符串转json和json转字符串
"""

data_str = '{"user": "liang","password": "chen123."}'
print(data_str,type(data_str))

data_json = json.loads(data_str)
print(data_json,type(data_json))

data_dict = {
    'user':'周杰伦',
    'password':'chen123.'
}
data_str2 = json.dumps(data_dict,ensure_ascii=False) #展示中文
print(data_str2,type(data_str2))