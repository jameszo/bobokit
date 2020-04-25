# Python Program Memo

## data

```
type(1)
isinstance(1, int)
float(2)
int(2.5)
11//2
fractions.Fraction(1, 3)
math.pi
slice
[n if n > 0 else 0 for n in mylist]
[n for n in mylist if n > 0]
(n for n in mylist if n > 0)
list(filter(is_int, values))
compress()
```

## file

```
os.remove(path)
```

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

## html

from bs4 import BeautifulSoup

```
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="sister"><b>$37</b></p>
<p class="story" id="p">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" >Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
and they lived at the bottom of a well.</p>
"""

soup = BeautifulSoup(html_doc, 'lxml')
html = soup.prettify()

#直接使用
print(soup.p)  #查找第一个p标签

#获取标签的名称
print(soup.head.name)  #获取head标签的名称

#获取标签的属性
print(soup.a.attrs)  #获取a标签中的所有属性
print(soup.a.attrs['href'])  #获取a标签中的href属性

#获取标签的内容
print(soup.p.text)

#嵌套选择
print(soup.html.head)

#子节点、子孙节点
print(soup.body.children)  #body所有子节点，返回的是迭代器对象
print(list(soup.body.children))  #强转成列表类型

print(soup.body.descendants)  #子孙节点
print(list(soup.body.descendants))  #子孙节点

#父节点、祖先节点
print(soup.p.parent)  #获取p标签的父亲节点
#返回的是生成器对象
print(soup.p.parents)  #获取p标签所有的祖先节点
print(list(soup.p.parents))

#兄弟节点
#找下一个兄弟
print(soup.p.next_sibling)
#找下面所有的兄弟，返回的是生成器
print(soup.p.next_siblings)
print(list(soup.p.next_siblings))

#找上一个兄弟
print(soup.a.previous_sibling)  #找到第一个a标签的上一个兄弟节点
#找到a标签上面的所有兄弟节点
print(soup.a.previous_siblings)  #返回的是生成器
print(list(soup.a.previous_siblings))o

#搜索文档树:

#字符串过滤器
p_tag = soup.find(name='p')
#找到所有标签名为p的节点
tag_s1 = soup.find_all(name='p')
#查找第一个class为sister的节点
p = soup.find(attrs={"class": "sister"})
#查找所有class为sister的节点
tag_s2 = soup.find_all(attrs={"class": "sister"})
#text
text = soup.find(text="$37")
#找到一个id为link2、文本为Lacie的a标签
a_tag = soup.find(name="a", attrs={"id": "link2"}, text="Lacie")

#正则过滤器
p_tag = soup.find(name=re.compile('p'))

#列表过滤器
tags = soup.find_all(name=['p', 'a', re.compile('html')])

#找到有id的p标签
p = soup.find(name='p', attrs={"id": True})

#方法过滤器
#匹配标签名为a、属性有id没有class的标签
def have_id_class(tag):
    if tag.name == 'a' and tag.has_attr('id') and tag.has_attr('class'):
        return tag

tag = soup.find(name=have_id_class)
```
