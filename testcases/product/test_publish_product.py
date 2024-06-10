# coding: utf-8
import pytest
import allure

from common.common_requests import Resquests

goods_info_list = [
    {
        "product_title": "新增商品-1",
        "product_stock": 1,
        "product_price": "0.9",
        "product_status": 1,
        "product_desc": "这是描述",
        "product_img":
            [
                "http://122.51.42.138:9090/product/product_img/17161856389256febbdc2-7de1-493e-948f-b8078d35f668"
            ]
    },
    {
        "product_title": "新增商品-aotu2",
        "product_stock": 1,
        "product_price": "0.9",
        "product_status": 1,
        "product_desc": "这是描述",
        "product_img":
            [
                "http://122.51.42.138:9090/product/product_img/17161856389256febbdc2-7de1-493e-948f-b8078d35f668"
            ]
    }

]


class TestApi(object):
    @allure.description('用户上传二手商品')
    @allure.epic('主页')
    @allure.feature('产品')
    @allure.story('新增二手商品')
    @pytest.mark.parametrize('goods_info', goods_info_list)
    def test_add_product(self, token, goods_info):
        with allure.step('登录获取token'):
            headers = {
                'token': token('chen')
            }

        with allure.step('新增二手商品'):

            res = Resquests(headers).post('/api/product/publish_product', json=goods_info)
            print(res.json())
        assert res.json()['code'] == 200
        assert res.json()['msg'] == '成功'
