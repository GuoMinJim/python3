# # 正则表达式
# import requests
# import re
# html = '''<div id="songs-list">
#     <h2 class="title">经典老歌</h2>
#     <p class="introduction">
#         经典老歌列表
#     </p>
#     <ul id="list" class="list-group">
#         <li data-view="2">一路上有你</li>
#         <li data-view="7">
#             <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
#         </li>
#         <li data-view="4" class="active">
#             <a href="/3.mp3" singer="齐秦">往事随风</a>
#         </li>
#         <li data-view="4" class="active">
#             <a href="/3.mp3" singer="齐秦1">往事2随风</a>
#         </li>
#         <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
#         <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
#         <li data-view="5">
#             <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
#         </li>
#     </ul>
# </div>'''
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# results = re.findall('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(results)
# if result:
#     print(result.group(1), result.group(2))
#
import requests
import re
html = '''<li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30324991/?icn=index-latestbook-subject" title="三口棺材">
                <img src="https://img3.doubanio.com/view/subject/m/public/s30014124.jpg" class=""
                  width="115px" height="172px" alt="三口棺材">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30324991/?icn=index-latestbook-subject"
                  title="三口棺材">三口棺材</a>
              </div>
              <div class="author">
                [美]约翰·迪克森·卡尔
              </div>
              <div class="more-meta">
                <h4 class="title">
                  三口棺材
                </h4>
                <p>
                  <span class="author">
                    [美]约翰·迪克森·卡尔
                  </span>
                  /
                  <span class="year">
                    2019-3
                  </span>
                  /
                  <span class="publisher">
                    新星出版社
                  </span>
                </p>
              </div>
            </div>
          </li>'''

content = requests.get('https://book.douban.com/').text
# print(content)
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
resulsts = re.findall(pattern,html)
for result in resulsts:
    url, name, author, date = result
    author = re.sub('\s', '', author)
    date = re.sub('\s', '', date)
    print(url, name, author, date)
# pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
# results = re.findall(pattern, content)
# for result in results:
#     url, name, author, date = result
#     author = re.sub('\s', '', author)
#     date = re.sub('\s', '', date)
#     print(url, name, author, date)