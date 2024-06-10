# coding:utf-8
from common.common_requests import Resquests
from common.yaml_config import GetConf


def login(user):
    username, password = GetConf().get_username_password(user)
    login_data = {
        'user': username,
        'password': password
    }
    login_res = Resquests().post('/api/user/login', json=login_data)
    return login_res