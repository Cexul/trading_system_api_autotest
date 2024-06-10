# coding: utf-8
import yaml
from common.tools import get_project_path,sep


"""
    读取yaml的配置文件
"""
# file = open('/Users/chenxuliang/PycharmProjects/trading_system_api_autotest/config/environment.yaml',encoding = 'utf-8')


# a = file.read()
# print(a)
# file.close()

# with open('/Users/chenxuliang/PycharmProjects/trading_system_api_autotest/config/environment.yaml','r',encoding='utf-8') as f:
#     a = f.read()
# print(a)
class GetConf(object):
    def __init__(self):
        project_path = get_project_path()
        with open(project_path+sep(['config','environment.yaml'],add_sep_before=True),'r',encoding='utf-8') as f:
            self.env = yaml.load(f,Loader=yaml.FullLoader) # 将字符串转化为字典或列表

    def get_username_password(self,user):
        return self.env['user'][user]['username'],self.env['user'][user]['password']

    def get_url(self):
        """
        测试地址
        :return:
        """
        return self.env['url']

    def get_mysql_config(self):
        return self.env['mysql']




if __name__ == '__main__':
    print(GetConf().get_username_password('jay'))
    print(GetConf().get_mysql_config())