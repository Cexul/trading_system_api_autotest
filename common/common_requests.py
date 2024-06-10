# coding:utf-8

import requests
from requests.adapters import HTTPAdapter

from common.yaml_config import GetConf
from common.deal_with_response import deal_with_res


class Resquests(object):
    def __init__(self, headers=None, timeout=10):
        """
        requests封装
        :param headers:
        :param timeout:
        """
        self.s = requests.Session()
        # 在session实例上挂载adapter实例，目的就是请求异常时，自动重试
        self.s.mount('http://', HTTPAdapter(max_retries=3))
        self.s.mount('https://', HTTPAdapter(max_retries=3))

        # 公共的请求头设置
        self.s.headers = headers
        self.timeout = timeout
        self.url = GetConf().get_url()

    def get(self, url, params=None):
        """
        GET
        :param url: 接口地址
        :param params: 一般get的参数都是放在URL查询参数里面
        :return:
        """
        res = self.s.get(self.url + url, params=params, timeout=self.timeout)
        deal_with_res(params,res)
        return res

    def post(self, url, data=None, json=None):
        """
        POST
        :param url: 接口地址
        :param data: 参数放在表单中
        :param json: 参数放在请求体中，一般是json
        :return:
        """
        if data:
            res = self.s.post(self.url + url, data=data, timeout=self.timeout)
            deal_with_res(data,res)
            return res
        if json:
            res = self.s.post(self.url + url, json=json, timeout=self.timeout)
            deal_with_res(json,res)
            return res
        res = self.s.post(self.url + url, timeout=self.timeout)
        deal_with_res(json,res)
        return res

    def put(self, url, data=None, json=None):
        """
        PUT
        :param url: 接口地址
        :param data: 参数放在params中
        :param json: 参数放在请求体里，一般是json
        :return:
        """
        if data:
            res = self.s.put(self.url + url, data=data, timeout=self.timeout)
            return res
        if json:
            res = self.s.put(self.url + url, json=json, timeout=self.timeout)
            return res
        return self.s.put(self.url + url, timeout=self.timeout)

    def delete(self, url, data=None, json=None):
        """
        DELETE
        :param data: 参数放在params里
        :param json: 参数放在boby中
        :return:
        """
        if data:
            res = self.s.delete(self.url + url, data=data, timeout=self.timeout)
            return res
        if json:
            res = self.s.delete(self.url + url, json=json, timeout=self.timeout)
            return res
        return self.s.delete(self.url + url, timeout=self.timeout)

    def __del__(self):
        """
        当实例被销毁时，释放掉session所持有的连接
        :return:
        """
        if self.s:
            self.s.close()
