# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# # from bs4 import BeautifulSoup
# # soup = BeautifulSoup(html,'lxml')
# # print(soup.prettify())
# # print(soup.title.string)
#
#
# # htmll = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """

# print(soup.title)
# print(soup.p)
# print(type(soup.p))
# print(soup.title.name) #这是拿到标签的名字

# print(soup.p.attrs['name'])
# print(soup.p['name'])

# print(soup.head.title.string)

#
# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """
# soup = BeautifulSoup(html,"lxml")
# # print(soup.p.contents)
# print(soup.p.children)
#
# for i,child in enumerate(soup.p.children):
#     print(i,child)


from bs4 import BeautifulSoup
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all('ul'))
# print()
# for ul in soup.find_all('ul'):
#     for li in ul.find_all('li'):
#         print(li)

# print(soup.find_all(attrs={'id':'list-1'}))
# print(soup.find_all(attrs={'name':'elements'}))
# print(soup.find_all(id="list-1"))
# print(soup.find_all(class_='panel-heading'))
# print(soup.find_all(text="Hello"))

# CSS选择器
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print()
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))
print()
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
for li in soup.select('li'):
    print(li.get_text())

