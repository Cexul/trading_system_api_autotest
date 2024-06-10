# coding:utf-8


import allure
from common.common_requests import Resquests


class TestApi(object):

    @allure.description('登录页面会员登录')
    @allure.epic('登录')
    def test_login(self):
        with allure.step('用户登录'):
            data = {
                'user': 'liang',
                'password': 'chen123.'
            }
            res = Resquests().post('/api/user/login', json=data)
            print('token的值是：', res.json()['data']['token'])
