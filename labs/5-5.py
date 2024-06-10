# coding : utf-8

import requests
from common.yaml_config import GetConf

username, password = GetConf().get_username_password()
url = GetConf().get_url()
data = {
    'user': username,
    'password': password
}
res = requests.post(url + '/api/user/login', json=data)
print(res.text)
