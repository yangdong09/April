import yaml,os

class Yaml:
    '''
    __filepath:读取yanml文件路径
    '''
    __filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.path.sep + 'config' + os.path.sep + 'api.yaml')
    def read_yaml(self):
        '''
        读取yaml文件内容,返回list格式文件
        :return: 返回读取的内容ya
        '''
        with open(Yaml.__filepath,encoding='utf-8') as fp:
            ya = yaml.load(fp,yaml.FullLoader)
        return ya


# 返回yaml文件内容如下：
'''
[{'name': '登录接口', 'request': {'method': 'get', 'url': 'http://www.baidu.com', 'params': {'keyword': 'yangdong'}}, 
'validate': [{'eq': {'status_code': 200}}, {'eq': {'message': 'process success'}}]}]
'''