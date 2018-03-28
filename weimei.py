import requests
from urllib.parse import urljoin
from parsel import Selector
import os
import random

base_url = 'http://www.55156.com/weimei/'
UserAgent_List = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
    "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
    "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
    "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
    "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00"
]


page_link = []

'''
    获取当前图片类的所有页数 
    返回list
    egg:http://www.55156.com/weimei/list_40_85.html
'''
def get_page_link(url):
    ua = random.choice(UserAgent_List)
    header = {
        'User-Agent': ua
    }
    print('get_page_link ',header)
    page_link.append(url)
    response = requests.get(url,headers=header)
    response.encoding = 'utf-8'
    html = Selector(response.text)
    next_page = html.xpath('//div[@class="pages"]/ul/li[last()-1]/a/@href')[0].extract()
    if '#' not in next_page:
        new_url = urljoin(url,next_page)
        get_page_link(new_url)
        # print(new_url)

    return page_link

'''
    获取每一页的图片链接
    返回list
    egg:http://www.55156.com/weimei/9487.html
'''
def get_img_link(url):
    img_link = []
    img_link.append(url)
    ua = random.choice(UserAgent_List)
    header = {
        'User-Agent': ua
    }
    response = requests.get(url,headers=header)
    response.encoding = 'utf-8'
    html = Selector(response.text)
    img_link = html.xpath('//div[@class="listBox"]/ul/li/a/@href').extract()
    return img_link
'''
    egg: http://www.55156.com/weimei/9487_5.html
'''
def save_orage_img(url):
    # orage_link = []
    page_link.append(url)
    ua = random.choice(UserAgent_List)
    header = {
        'User-Agent': ua
    }
    print('save_orage_img',header)
    response = requests.get(url,headers=header)
    response.encoding = 'utf-8'
    html = Selector(response.text)
    orage_url = html.xpath('//div[@class="articleBody"]/p/a/img/@src')[0].extract()
    orage_name = html.xpath('//div[@class="articleBody"]/p/a/img/@alt')[0].extract()
    title = html.xpath('//div[@class="articleTitle"]/h1/text()')[0].extract()
    res = requests.get(orage_url,headers=header)
    orage = res.content
    try:
        if '(' not in title:
            path = os.path.abspath('.') + '\\imgages\\' + title + '\\'
            if not os.path.exists(path):
                os.makedirs(path)
            file = path + orage_name + '.jpg'
            with open(file, 'wb') as f:
                f.write(orage)
            print('%s  首页写入完成' % title)

        else:
            dir = title.split('(')[:-1][0]
            path = os.path.abspath('.') + '\\imgages\\' + dir + '\\'
            # print("path1",path)
            # if os.path.exists(path):
            file = path + orage_name + '.jpg'
            with open(file, 'wb') as f:
                f.write(orage)
                print('%s  写入完成' % title)

        next_page = html.xpath('//div[@class="pages"]/ul/li[last()]/a/@href')[0].extract()

        if '#' not in next_page:
            new_url = urljoin(url,next_page)
            save_orage_img(new_url)
            print('下一页 %s' %next_page)
    except Exception as e:
        print('只有一张')


def test_get_page_link():
    # 获得所有页数的url
    url = base_url
    link = get_page_link(url)
    print(link)

def test_get_img_link():
    url = 'http://www.55156.com/weimei/list_40_85.html'
    link = get_img_link(url)
    print(link)

def test3():
    page = 'http://www.55156.com/weimei/9487_5.html'
    save_orage_img(page)


def main():
    link = get_page_link(base_url)
    for page in link:
        img_link = get_img_link(page)
        for img in img_link:
            save_orage_img(img)
        # break

main()