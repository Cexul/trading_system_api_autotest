# coding:utf-8

import requests
import allure

from common.tools import sep,get_project_path


class TestApi(object):
    @allure.feature('market')
    @allure.story('download_img')
    @allure.description('下载图片')
    def test_download_img(self,token):
        headers ={
            'token':token('jay')
        }
        res = requests.get(
            "http://122.51.42.138:9090/product/product_img/16891322757521b47feac-40bd-45ea-a1f9-0634a97911e0",
            headers=headers
        )
        download_file_path = get_project_path()+sep(['img','download_file.jpg'],add_sep_before=True)
        with open(download_file_path,'wb')as f:
            f.write(res.content)