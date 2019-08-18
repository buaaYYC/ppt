# coding=utf-8
import json
import shutil
import os
import re
import urllib
from urllib import request
import bs4 as bs

def pic_extract(url):
    """
    抓取当前网页的图片
    :param url:
    :return:
    """
    if os.path.exists("image1"):
        for f in os.listdir('image1'):
            print(f)
            os.remove("image1/" + f)
    page = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(page, 'lxml')
    # print(soup)
    soup_urls = soup.find_all("img")
    print(soup_urls)
    listurls = []
    for u in soup_urls:
        #     print(u)
        try:
            if u["src"]:
                print(u["src"])
                listurls.append(u["src"])
            elif u["alt_src"]:
                print(u["alt_src"])
                listurls.append(u["alt_src"])
        except:
            print("no url")
            continue
    i = 0
    for url in listurls:
        # print(url)
        try:
            response = request.urlopen(url)
        except:
            continue
        image = response.read()
        if not os.path.exists("image1"):
            os.mkdir("image1")
        dir = "image1/image_" + str(i) + ".jpg"
        f = open(dir, "wb")
        f.write(image)
        i += 1

if __name__=="__main__":
    #
    # url = "https://www.toutiao.com/a6726291982190117387/"
    # pic_extract(url)
    pass
