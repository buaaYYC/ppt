import bs4 as bs
import urllib.request
import re
# from __future__ import print_function
import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import sys
try:
    sys.setdefaultencoding('utf-8')
except:
    pass


def translate(str):

    line = str.strip() # 处理前进行相关的处理，包括转换成Unicode等
    print(100*"#")
    p2 = re.compile(r'[^\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5
    zh = " ".join(p2.split(line)).strip()
    zh = ",".join(zh.split())
    texts = ""
    for setence in zh.split(","):
        if len(setence)<10:
            texts += setence + ","
        else:
            texts += setence + "。"
    outStr = texts  # 经过相关处理后得到中文的文本
    return outStr

url = "https://www.toutiao.com/a6726134868779991565/"
def article_extract(url):
    page = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(page,'lxml')
    #知乎文章的题目
    zihu_title = soup.html.head.title.text

    t1 = soup.find_all("p")
    texts = ""
    for sentence in t1:
        try:
            texts += sentence.contents[0].string
        except:
            continue
    if len(t1)<1:
        texts1 = soup.get_text()
        texts1 = translate(texts1)
        texts = texts1
    #知乎文章的内容
    return zihu_title,texts

# title,texts = article_extract(url)
#
# print("题目：",title)
# print("文本内容：",texts)
# # f = open("article.txt",'a')
# # f.write(texts)
# tr4w = TextRank4Keyword()
# tr4w.analyze(text=texts ,lower=True, window=2)   # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
# tr4s = TextRank4Sentence()
# tr4s.analyze(text=texts, lower=True, source = 'all_filters')
# print( '关键词：' )
# word_nu = 0
# for item in tr4w.get_keywords(10, word_min_len=2):
#     print(item.word, item.weight)
# print()
# print( '摘要：' )
# for item in tr4s.get_key_sentences(num=5):
#     print(item.index, item.weight, item.sentence)