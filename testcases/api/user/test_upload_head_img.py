# coding: utf-8
from urllib3 import encode_multipart_formdata
import allure

from common.tools import sep,get_project_path
from common.common_requests import Resquests



class TestApi(object):
    @allure.feature('product')
    @allure.story('upload_img')
    @allure.description('上传头像图片')
    def test_upload_img(self,token):
        img_path = get_project_path()+sep(['img','upload_file.jpg'],add_sep_before=True)
        file_data ={
            'file':('upload_img',open(img_path,'rb').read())
        }
        encode_data = encode_multipart_formdata(file_data)
        # print(encode_data)
        data = encode_data[0]
        headers = {
            'token':token('jay'),
            'Content-Type':encode_data[1]
        }
        res = Resquests(headers).post('/api/user/upload_head_img',data=data)
        print(res.json())
        assert res.json()['code']==200
        assert res.json()['msg']=='成功'


