# coding:utf-8
import allure

"""
    allure.attach测试报告中添加附件，补充测试结果。附件格式可以是txt、jpg等，附件内容通常是测试数据、截图等
"""


def deal_with_res(data, res):
    # 请求url
    request_url = str(res.request.url)
    allure.attach(request_url, '请求url')

    # 请求方法
    request_method = str(res.request.method)
    allure.attach(request_method, '请求方法')

    # 请求header
    request_headers = str(res.request.headers)
    allure.attach(request_headers, '请求头')

    # 入参报文
    request_data = str(data)
    allure.attach(request_data, '入参报文')

    # 响应时间
    response_time = str(res.elapsed.total_seconds() * 1000)
    allure.attach(response_time, '响应时间')

    # 状态码
    status_code = str(res.status_code)
    allure.attach(status_code, '状态码')

    # 响应报文
    response_text = str(res.text)
    allure.attach(response_text, '响应报文')
