import pytest,requests
from April_fourth.config.read_yaml import Yaml
from jsonpath import jsonpath
from April_fourth.utils.assert1 import Assert



class TestLogin:

    @pytest.mark.parametrize('arg',Yaml().read_yaml())
    def test_login(self,arg):

        a = jsonpath(arg ,'$..status_code')
        Assert().asser_status(200,a[0])

        # req = requests.post(url='',)


if __name__ == '__main__':
    pytest.main(['-vs'])