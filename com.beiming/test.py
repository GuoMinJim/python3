# import socket
# a = 0
# while not a:
#     a = 13
#     print("fuck u")
#
# import django
import requests

response = requests.get("http://www.baidu.com")
print(response.text)