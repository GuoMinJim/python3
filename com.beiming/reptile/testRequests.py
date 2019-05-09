# response = requests.get("http://www.baidu.com")
# print(response.text)
# print(response.headers)
import requests
# response1 = requests.get("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1557144701070&di=0a266146e7682b3b248515320289df13&imgtype=0&src=http%3A%2F%2Fdiskingdom.com%2Fwp-content%2Fuploads%2F2016%2F06%2FH_alternate.png")
# with open("E://Mi//1.png",'wb') as f:
#     f.write(response1.content)
#     f.close()

from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")  