import requests
import random
import re
from bs4 import BeautifulSoup

content = requests.get('http://www.qiushibaike.com').content
soup = BeautifulSoup(content, 'html.parser')
for div in soup.find_all('div',{'class':'content'}):
    print div.text.strip()

def demostr():
    stra = 'hello zjs'
    seta = set((1, 2, 3))
    setb = set((1, 2))
    #print 1, seta + setb
    print 2, stra.endswith('zjs')
    print 3, random.random()
    random.seed(1)
    print 4, random.random()
def demo_re():
    str = 'abc123'
    p1 = re.compile('[\d]+')
    print 1, p1.findall(str)
if __name__ == '__main__':
    print 'hello nowcoder'
    #demostr()
    demo_re()
