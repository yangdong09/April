import json
from April_fourth.log.log import logger
class Assert:

    def asser_status(self,code,asser_code):
        try:
            assert code == asser_code
            return True
        except Exception:
            logger.error('请求状态码对比失败，请求状态吗{0}，断言状态码{1}'.format(code,asser_code))

    def assert_json_data(self,json_data):
        try:
            json.loads(json_data)
            print(nihao)
            # return True
        except Exception:
            logger.error('返回格式错误，应该返回格式json，实际返回格式错误{0}'.format(type(json_data)))

