html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
         <p></p>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq

# 字符串初始化
# doc = pq(html)
# print(doc('li'))

# URL初始化
# doc = pq(url='http://www.baidu.com')
# print(doc('head'))

#文件初始化
# doc = pq(filename='demo.html')
# print(doc('li'))

# 基本CSS选择器
# doc = pq(html)
# print(doc('#container .list li'))

# 查找元素
#  子元素
# doc = pq(html)
# items = doc('.list')
# print(type(items))
# print(items)
# # lis = items.find('li')
# # print(type(lis))
# # print(lis)
# lis = items.children()
# print(type(lis))
# print(lis)
#
# liss = items.children('.active')
# print(liss)

# 父元素
# doc = pq(html)
# items = doc('.list')
# container = items.parent()

# 遍历
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)

# lis = doc('li').items()
# print(type(lis))
# for li in lis:
#     print(li.text())

# 获取信息
# 获取属性

doc = pq(html)
# a = doc('.item-0.active a')
# print(a)
# print(a.attr('href'))
# print(a.attr.href)

# li = doc('.item-0.active')
# print(li)
# print(li.html())

# DOM操作

#操作class
li = doc('.item-0.active')
# print(li)
# li.remove_class('active')
# print(li)
# li.add_class('active')
# print(li)

# CSS操作
# print(li)
# li.attr('name','link')
# print(li)
# li.css('font-size','14px')
# print(li)

# REMOVE

# html = '''
# <div class="wrap">
#     Hello, World
#     <p>This is a paragraph.</p>
#  </div>
# '''
#
# doc = pq(html)
# wrap = doc('.wrap')
# print(wrap.text())
# wrap.find('p').remove()
# print(wrap.text())

# 其他DOM方法 伪类选择器
doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)

