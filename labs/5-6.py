# coding : utf-8

import requests
from common.yaml_config import GetConf

url = GetConf().get_url()
token= "JWT eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0cmFkaW5nX3N5c3RlbSIsImlkIjoyOSwiaWF0IjoxNzE1OTM5MDk0LCJleHAiOjE3MTY1NDM4OTR9.cmRchy2Ria8AObQo98DsQMvRB2uhGLc_dKyZWJdKw3s"
headers = {
    "token": token
}
res = requests.post(url+'/api/wallet/get_wallet_info',headers=headers)
print(res.text)