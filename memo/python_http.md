# Python HTTP

## requests

import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

```
请求：
r = requests.request(method='get', url='http://127.0.0.1:8000/test/', params="k1=v1&k2=水电费&k3=v3&k3=vv3")
r = requests.get/post/put/delete/head/options('https://github.com/Ranxf', timeout=(3, 3), allow_redirects=False, auth=HTTPBasicAuth/HTTPDigestAuth('user', 'passwd'))
r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})
r = requests.post('https://api.github.com/some/endpoint', data=json.dumps({'some': 'data'}))

headers = {'content-type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
cookie = {'key':'value'}
r = requests.post('https://api.github.com/some/endpoint', headers=headers, cookies=cookie)

url = 'http://m.ctrip.com'
files = {'file': open('report.xls', 'rb')}
#files = {'file': ('report.jpg', open('/home/lyb/sjzl.mpg', 'rb'))}     #显式的设置文件名
#files = {'file': ('test.txt', b'Hello Requests.')}                     #必需显式的设置文件名
upload_data={"parentId":"","fileCategory":"personal","fileSize":179,"fileName":"summer_text_0920.txt","uoType":1}
r = requests.post(url, upload_data, files=files)

proxies = {
           "http": "http://user:pass@10.10.1.10:3128/",
           "https": "http://10.10.1.100:4444",
          }
r = requests.get('http://m.ctrip.com', proxies=proxies)

1、不管json是str还是dict，如果不指定headers中的content-type，默认为application/json
2、data为dict时，如果不指定content-type，默认为application/x-www-form-urlencoded，相当于普通form表单提交的形式
3、data为str时，如果不指定content-type，默认为text/plain
4、json为dict时，如果不指定content-type，默认为application/json
5、json为str时，如果不指定content-type，默认为application/json
6、用data参数提交数据时，request.body的内容则为a=1&b=2的这种形式，用json参数提交数据时，request.body的内容则为'{"a": 1, "b": 2}'的这种形式


响应：
r.encoding                       #获取当前的编码
r.encoding = 'utf-8'             #设置编码
r.raw                            #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read()
r.status_code                    #响应状态码
r.headers                        #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
r.request.headers
r.content                        #以字节形式（二进制）返回。字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩。
r.text                           #以encoding解析返回内容。字符串方式的响应体，会自动根据响应头部的字符编码进行解码。
r.ok                             #查看r.ok的布尔值便可以知道是否登陆成功
r.json()                         #Requests中内置的JSON解码器，以json形式返回,前提返回的内容确保是json格式的，不然解析出错会抛异常
r.raise_for_status()             #失败请求(非200响应)抛出异常
r.cookies
r.history

示例：
    from http.cookiejar import CookieJar
    from http.cookiejar import Cookie

    obj = CookieJar()
    obj.set_cookie(Cookie(version=0, name='c1', value='v1', port=None, domain='', path='/', secure=False, expires=None,
                          discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False,
                          port_specified=False, domain_specified=False, domain_initial_dot=False, path_specified=False)
                   )
    requests.request(method='POST',
                     url='http://127.0.0.1:8000/test/',
                     data={'k1': 'v1', 'k2': 'v2'},
                     cookies=obj)

    r = requests.get(url, stream=True)
    with open('test', 'wb') as fd:
        for chunk in r.iter_content(1024 * 100):
            fd.write(chunk)

    from contextlib import closing
    with closing(requests.get('http://httpbin.org/get', stream=True)) as r:
        for i in r.iter_content():
            print(i)

    session = requests.Session()
    i1 = session.get(url="http://dig.chouti.com/help/service")
    i2 = session.post(
        url="http://dig.chouti.com/login",
        data={
            'phone': "8615131255089",
            'password': "xxxxxx",
            'oneMonth': ""
        }
    )
    i3 = session.post(
        url="http://dig.chouti.com/link/vote?linksId=8589623",
    )
    print(i3.text)
```

## https
