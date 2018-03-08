# python 3.7
#爬取网站内容
import re
import urllib
import urllib.request
import urllib.parse
from collections import deque
from urllib.request import Request,urlopen
from urllib.error import URLError,HTTPError
import gzip
crawlfiles=0
def save(data):
    global crawlfiles
    crawlfiles+=1
    file = open(''.join(("d:\\work\\learngit\\learn\\Reptiledata\\fuck",str(crawlfiles),".txt")),'wb')
    file.write(data.encode("utf-8"))
    file.close()
user_agent = "mozilla/5.0(Windows NT 10.0;win64;x64;rv:58.0)Gecko/20100 10 1 Firefox/58.0"
#Request.add_header(user_agent,values)
values = {
    'act': 'login'
}
queue = deque()
visited = set()
url = "http://www.pfc.edu.cn"
queue.append(url)
cnt = 0
while queue:
    url = queue.popleft()
    visited |= {url}
    print('已经抓取：'+str(cnt)+'   正在抓取 <---'+url)
    cnt += 1
    try:
        urlop = urllib.request.urlopen(url,timeout=10)
        if 'html' not in urlop.getheader('Content-Type'):
            continue
        # TODO:为避免程序异常终止，用try..catch处理异常
        data = urlop.read().decode('utf-8')
    except HTTPError as e:
        print("The server couldn't fulfill the request.")
        print('Error code:',e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason:',e.reason)
    except:
        continue
    def ungzip(data):
        try:
            print('正在解压。。。。。。')
            data = gzip.decompress(data)
            print('解压完毕！')
        except:
            print('未经压缩，不需解压！')
        return data
    def getOpener(head):
        #TODO deal with the Cookies
        cj = http.cookiejar.CookieJar()
        pro = urllib.request.HTTPCookieProcessor(cj)
        opener = urllib.request.build_opener(pro)
        header = []
        for key,value in head.items():
            elem = (key, value)
            header.append(elem)
            opener.addheaders = header
        return opener
    #TODO:正则表达式提取页面中的全部队列，来判断是否已经访问过，然后加入待爬队列
    linkre = re.compile('href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列 --->   '+ x)
    try:
        save(data)
    except:
        continue