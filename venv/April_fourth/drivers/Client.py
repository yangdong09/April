import requests

class Method:
    GET ='get'
    POST = 'post'

class BodyType:
    '''
    枚举：将所有的请求类型列出来
    '''
    FORM_DATA = 'form-data'
    JSON = 'json'
    XML = 'xml'
    URL_ENCODE = 'urlencoded'

class Client:
    def __init__(self,url,method,bodytype=None,params=None):
        '''
        初始化参数，将公共部分传入
        :param url: 请求地址：http//www.baidu.com
        :param method: 请求方法：get、post
        :param bodytype: post请求类型Content-Type：json、xml、urlencoded、form-data
        :param params: get请求参数将？后面的部分写成字典形式：{’id‘：’1‘，’name‘，’yang‘} 等同于连接上 id=1&name=yang
        '''
        self.__url = url
        self.__method = method
        self.__bodytype = bodytype
        self.__params = params
        '''
            初始化时设置的默认私有变量参数，外部要访问，私有变量不让外部直接访问，可以用set和get在外部访问
        '''
        self.__headers = {}
        self.__body= {}
        self.__response = None


    def add_headers(self,name,value):
        '''
        添加头部信息：add_header('User-Agent','Mozilla/5.0')
        :param name: 请求头名称：User-Agent
        :param value: 请求头值：Mozilla/5.0
        :return:
        '''
        sefl.__headers[name] = value

    '''第二种添加headers的方法，@property、@headers.setter这两个必须一起用'''
    @property
    def headers(self):
        return self.__headers
    @headers.setter
    def headers(self,headers):
        self.__headers =headers

    def send(self):
        '''
        这里封装get和post方法
        :return:
        '''
        if self.__method == Method.GET:
            self.__response = requests.get(url=self.__url,headers=self.__headers)
        elif self.__method ==Method.POST:
            if self.__headers == BodyType.URL_ENCODE:
                self.add_headers('Content-Type','application/x-www-form-urlencoded')
                self.__response = requests.post(url=self.__url,headers=self.__headers,data=self.__body)

            if self.__headers ==BodyType.FORM_DATA:
                self.add_headers('Content-Type', 'multipart/form-data')
                self.__response = requests.post(url=self.__url,headers=self.__headers,data=self.__body)
            if self.__headers ==BodyType.XML:
                self.add_headers('Content-Type', 'application/xml')
                self.__response =requests.post(url=self.__url,headers=self.__headers,data=self.__body.get('text'))
            if self.__headers ==BodyType.JSON:
                self.add_headers('Content-Type', 'application/json')
                self.__response=requests.post(url=self.__url,headers=self.__headers,json=self.__body)
            else:
                raise Exception('post暂不支持该格式')
        else:
            raise Exception('目前只支持"get"和"post"格式请求')

    @property
    def text(self):
        if self.__response:
            return self.__response.text
        else:
            raise Exception('当前请求没有返回值')

    @property
    def code(self):
        if self.__response:
            return self.__response.status_code
        else:
            raise Exception('当前没有返回code')


    @property
    def response(self):
        '''
        外部调用使用该方法的返回值
        :return:
        '''
        return self.__response


client = Client('http://www.baidu.com','get')
client.send()
a = client.code
print(a)
