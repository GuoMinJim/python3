# 抓取猫眼前100榜单  使用requests & regex爬取豆瓣评分前100
import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
def get_one_page(url):
    try:
        respoonse = requests.get(url, headers)
        if respoonse.status_code == 200:
            return respoonse
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
               + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
               + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5]+item[6]
        }

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html.text):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    #单线程
    # for i in range(10):
    #     main(i*10)
    # 多线程
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])
    pool.close()
    pool.join()