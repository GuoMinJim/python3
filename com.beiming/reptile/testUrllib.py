# import urllib.request
#
# request = urllib.request.Request('http://python.org')
# response = urllib.request.urlopen(request)
# # print(response.read().decode('utf-8'))
#
#
# #POST请求
# from urllib import request,parse
#
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
#     'Host':'httpbin.org'
# }
# dict = {
#     'name':'Germey'
# }
#
# data = bytes(parse.urlencode(dict),encoding='utf8')
# req = request.Request(url= url,data=data,headers=headers,method='POST' )
# response = request.urlopen(req)
# # print(response.read().decode('utf-8'))


# #代理
# import urllib.request
#
# proxy_handler = urllib.request.ProxyHandler({
#     'http':'http://127.0.0.1:8080',
#     'https':'https://127.0.0.1:8080'
# })
# openerR = urllib.request.build_opener(proxy_handler)
# responseR = openerR.open('http://httpbin.org/get')
# print(responseR.read())


# Cookie
# import http.cookiejar,urllib.request
#
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# openerC = urllib.request.build_opener(handler)
# responseC = openerC.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+"="+item.value)

# URL解析
from urllib.parse import urlparse
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)

#jupyter notebook