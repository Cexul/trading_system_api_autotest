# coding : utf-8

import requests
from common.yaml_config import GetConf

# url = GetConf().get_url()
# token= "JWT eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0cmFkaW5nX3N5c3RlbSIsImlkIjoyOSwiaWF0IjoxNzE1OTM5MDk0LCJleHAiOjE3MTY1NDM4OTR9.cmRchy2Ria8AObQo98DsQMvRB2uhGLc_dKyZWJdKw3s"
# headers = {
#     'token' :token
# }
# res = requests.get(url+'/api/router/router_list/',headers=headers)
# print(res.text)

url = 'http://www.imooc.com/search/coursesearchconditions'
params = {
    'words':'人工智能'
}
res = requests.get(url,params=params)
print(res.text)