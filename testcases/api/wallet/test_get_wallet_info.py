# coding:utf-8
import allure

from common.common_requests import Resquests


class TestApi(object):

    @allure.description('调用获取钱包接口')
    @allure.epic('主页')
    @allure.feature('用户信息')
    @allure.story('用户钱包信息')
    @allure.tag('余额')
    def test_get_wallet_info(self, token):
        with allure.step('登录'):
            headers = {
                'token': token('jay')
            }
        with allure.step('调用获取用户钱包信息接口'):
            res = Resquests(headers).post('/api/wallet/get_wallet_info')
            print(res.json())
        with allure.step('断言'):
            assert res.json()['code'] == 200
            assert res.json()['msg'] == '成功'
