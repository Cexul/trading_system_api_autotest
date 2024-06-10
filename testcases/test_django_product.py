from common.common_requests import Resquests


class TestApi(object):
    def test_django_product_get(self):

        res = Resquests().get('/api/product/product_list')
        print(res.json())