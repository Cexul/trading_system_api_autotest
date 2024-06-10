# coding:utf-8
import json

import pytest
import os

from common.login import login
from common.tools import sep, get_project_path
from common.mysql_operate import MysqlOperate


@pytest.fixture()
def token():
    def _token(user):
        # 判断存放token的目录时候存在，不存在则自动创建
        token_json_dir = sep([get_project_path(), 'token_dir'])
        if not os.path.exists(token_json_dir):
            os.mkdir(token_json_dir)
        token_json_path = sep([token_json_dir, user + '_token.json'])
        if not os.path.exists(token_json_path):
            # 文件不存在，调用登录接口，并把token写入json文件
            print(f'{user}对应的token的json文件不存在，调用登录接口')
            token = login(user).json()['data']['token']
            print(f'写入{user}对应的token的json文件')
            with open(token_json_path, 'w+') as write_token:
                write_token.write(json.dumps({'token': token}))
            return token
        else:
            # 文件存在则取出token的值
            print(f'{user}对应的token的json文件已存在，读取json文件中的token')
            with open(token_json_path, 'r') as token_info:
                token = json.loads(token_info.read())
                return token['token']

    return _token


@pytest.fixture()
def get_balabce_from_db():
    sql = 'select balance from wallet where user_=3;' # 数据库建设未完成，查询会报错
    db_balance = MysqlOperate().query(sql)[0][0]
    print('db_balance:',db_balance)
    yield db_balance