# coding : utf-8

import os

def get_project_path():
    """
    获取项目目录
    :return:
    """
    project_name = 'trading_system_api_autotest'
    file_path = os.path.dirname(__file__) # os.path.dirname((__file__)就是得到当前文件的绝对路径
    # print(file_path)
    # print(file_path.find(project_name))
    return file_path[:file_path.find(project_name)+len(project_name)] #拿到trading_system_api_autotest项目所在文件路径的索引

def sep(path,add_sep_before=False,add_sep_after=False):
    """
    系统分隔符
    :param path: 路径列表，类型为列表数组 ['chen','cu']
    :param add_sep_before: 是否需要在拼接的路径前加一个分隔符
    :param add_sep_after: 是否需要在拼接的路径后面加一个分隔符
    :return:
    """
    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path # os.spe是分隔符

    if add_sep_after:
        all_path = all_path + os.sep
    return all_path




if __name__ == '__main__':
    print(get_project_path())