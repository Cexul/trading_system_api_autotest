# coding:utf-8
from common.common_requests import Resquests
import allure


class TestApi(object):

    @allure.description('获取主页菜单信息')
    @allure.epic('主页')
    def test_get_left_menu_info(self, token):
        with allure.step('登录获取token'):
            headers = {
                'token': token('jay')
            }
        with allure.step('查询菜单信息'):
            res = Resquests(headers).get('/api/router/router_list')
            print(res.json())
