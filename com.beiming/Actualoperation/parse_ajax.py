# 分析ajax抓取今日头条街拍美图

import json
import os
from urllib.parse import urlencode
import pymongo
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
import re
from multiprocessing import Pool
from hashlib import md5
from json.decoder import JSONDecodeError
from config import *
import time
from requests.exceptions import RequestException

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'cookie': 'tt_webid=6689205973414348291; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=16a9f61bb36384-09033883cfb01d-3b654406-240000-16a9f61bb372e6; tt_webid=6689205973414348291; csrftoken=f20f71bd3829e96e0cd3e11113ed13c8; s_v_web_id=658ac4463545f1efc102b1b80cf672ce; passport_auth_status=5571efade0d632b7e5a222a2ac400566; sso_uid_tt=780815266c64e9bd5f03d7cc8c0d9f57; toutiao_sso_user=187b273323932ba1772ff84f0f1e517f; login_flag=52b55ea72a5dcd02883224071bc8498a; sessionid=1f59a2c0d149292108c37a634ce3102e; uid_tt=3099c9a5285bed8cdaef267204781685; sid_tt=1f59a2c0d149292108c37a634ce3102e; sid_guard="1f59a2c0d149292108c37a634ce3102e|1557452294|15552000|Wed\054 06-Nov-2019 01:38:14 GMT"; CNZZDATA1259612802=232085659-1557448136-%7C1557453536; __tasessionId=918nct9vq1557454715194'
}

def get_page_index(offset, keyword):
    data = {
        'autoload': 'true',
        'count': 20,
        'cur_tab': 3,
        'format': 'json',
        'keyword': keyword,
        'offset': offset,
        'timestamp': int(time.time()*1000)
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        'cookie': 'tt_webid=6689205973414348291; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=16a9f61bb36384-09033883cfb01d-3b654406-240000-16a9f61bb372e6; tt_webid=6689205973414348291; csrftoken=f20f71bd3829e96e0cd3e11113ed13c8; s_v_web_id=658ac4463545f1efc102b1b80cf672ce; passport_auth_status=5571efade0d632b7e5a222a2ac400566; sso_uid_tt=780815266c64e9bd5f03d7cc8c0d9f57; toutiao_sso_user=187b273323932ba1772ff84f0f1e517f; login_flag=52b55ea72a5dcd02883224071bc8498a; sessionid=1f59a2c0d149292108c37a634ce3102e; uid_tt=3099c9a5285bed8cdaef267204781685; sid_tt=1f59a2c0d149292108c37a634ce3102e; sid_guard="1f59a2c0d149292108c37a634ce3102e|1557452294|15552000|Wed\054 06-Nov-2019 01:38:14 GMT"; CNZZDATA1259612802=232085659-1557448136-%7C1557453536; __tasessionId=918nct9vq1557454715194'
    }
    url = 'https://www.toutiao.com/api/search/content/?'+urlencode(data)
    try:
        response = requests.get(url, headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None

def get_page_detail(url):
    url = str(url)
    new_url = url.replace('668','a668')
    print(new_url)
    try:
        response = requests.get(new_url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错')
        return None

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def parse_page_detail(html,url):
    soup = BeautifulSoup(html, 'lxml')
    result = soup.select('title')
    title = result[0].get_text() if result else ''
    pattern = re.compile('gallery: JSON.parse\("(.*)"\)', re.S)
    result = re.search(pattern, html)
    if result:
        data = json.loads(result.group(1))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            return {
                'title':title,
                'url':url,
                'images':images
            }

def main():
    html = get_page_index(20, '街拍')
    for url in parse_page_index(html):
        print(url)
        html = get_page_detail(url)
        print(html)
        # if html:
        #     result = parse_page_detail(html,url)
        #     print(result)
if __name__ == '__main__':
    main()
