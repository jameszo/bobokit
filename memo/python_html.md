# Python HTML

## BeautifulSoup

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
