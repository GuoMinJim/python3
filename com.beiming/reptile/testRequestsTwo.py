# requests 实例引入
import requests
# response = requests.get('http://www.baidu.com')
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# print(response.cookies)

# 各种请求方式
# POST,GET,DELETE,HEAD,OPTIONS

# 带参数的GET请求
# response = requests.get("http://httpbin.org/get?name=germey&age=22")
# print(response.text)

# data = {
#     'name':"jgm",
#     'age':'22'
# }
# response = requests.get('http://httpbin.org/get',data)
# print(response.text)

# 解析JSON
# import json
# response = requests.get("http://httpbin.org/get")
# print(type(response.text))
# print(response.json())
# print(json.loads(response.text))
# print(type(response.json()))

# 解析二进制数据
# response = requests.get("https://github.com/favicon.ico")
# print(type(response.text),type(response.content))
# print(response.text)
# print(response.content)
# 下载二进制数据到本地
response = requests.get("https://pic2.zhimg.com/v2-cc2a89915761263d84d1ea530e7f91f0_b.gif")
with open('aa.gif','wb') as f:
    f.write(response.content)
    f.close()

# 基本POST请求
# data = {
#     'name':'jgm',
#     'age':'222'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# response = requests.post('http://httpbin.org/post',data=data,headers=headers)
# print(response.text)

# 状态码判断
# response = requests.get('http://www.jianshu.com/hello.html')
# exit() if not response.status_code == 200 else print("Request bad Successful")

# response = requests.get('http://www.jianshu.com')
# exit() if not response.status_code != 200 else print('Request Successfully')


# 高级操作

#文件上传
# files = {'file':open('favicon.ico','rb')}
# response = requests.post('http://httpbin.org/post',files=files)
# print(response.text)

#获取cookie
# response = requests.get("http://www.baidu.com")
# print(response.cookies)
# for key,value in response.cookies.items():
#     print(key+'='+value)

# 会话维持
# 模拟登陆

# requests.get('http://httpbin.org/cookies/set/number/123456789')
# response = requests.get('http://httpbin.org/cookies')
# print(response.text)

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)

#证书验证
# print(requests.get('https://www.12306.cn').status_code)
# response = requests.get('https://www.12306.cn')
# print(response.status_code)

# import urllib3
# urllib3.disable_warnings()
# print(requests.get('https://www.12306.cn',verify=False).status_code)

# print(requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key')).status_code)

#代理设置
# proxies = {
#   "http": "http://127.0.0.1:9743",
#   "https": "https://127.0.0.1:9743",
# }

# response = requests.get("https://www.taobao.com", proxies=proxies)
# print(response.status_code)

# 认证设置
# from requests.auth import HTTPBasicAuth
# from requests.exceptions import ReadTimeout
# try:
#     r = requests.get("http://httpbin.org/get", auth=HTTPBasicAuth('user', '123'), timeout=0.5)
#     print(r.status_code)
# except ReadTimeout:
#     print("Timeout")
#
# # 超时设置
# from requests.auth import HTTPBasicAuth
# from requests.exceptions import ReadTimeout
# try:
#     r = requests.get("http://httpbin.org/get", auth=HTTPBasicAuth('user', '123'), timeout=0.5)
#     print(r.status_code)
# except ReadTimeout:
#     print("Timeout")