import re
import urllib
import urllib.request
import urllib.parse
from collections import deque
import os
import os.path
def save(data :str):
    file = open("d:\\work\\learngit\\learn\\Reptiledata\\fuck.txt",'wb')
    file.write(data.encode("utf-8"))
    file.close()
user_agent = "mozilla/5.0(Windows NT 10.0;win64;x64;rv:58.0)Gecko/20100 10 1 Firefox/58.0"
values = {
'act':'login'
}
headers = {'User-Agent':user_agent}
url = "http://www.baidu.com"
queue = deque()
visited = set()
queue.append(url)
cnt = 0
while queue:
    cnt += 1
    urlop = urllib.request.urlopen(url)
    data = urlop.read().decode('utf-8')
linkre = re.compile('href="(.+?)"')
for x in linkre.findall(data):
    if 'http' in x and x not in visited:
        queue.append(x)
        print('加入队列 ----->   '+ x)

