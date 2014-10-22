__author__ = 'huafeng'
#coding:utf-8
import codecs
import urllib2
import urllib
import time
import os
PATH = os.path.dirname(os.path.abspath(__file__))
def read_familyname_file():
    filename = os.path.join(PATH, 'data', 'all_familyname_word_pinyin.txt')
    with codecs.open(filename)as f:
        temp_familyname_list = []
        for word in [item.split('\t')[0].strip() for item in f.readlines()]:
            temp_familyname_list.append(word)
        return temp_familyname_list

# def read_html():
#     search_word_list = read_familyname_file()
#     failed_filename = os.path.join(PATH, 'log', 'failed_search_word_url')
#     crawled_filename = os.path.join(PATH, 'log', 'crawled_search_word')
#     word_content = os.path.join(PATH, 'out', 'familyname_content')
#     with codecs.open(failed_filename, mode='wb', encoding='utf-8') as failed_wf,\
#         codecs.open(crawled_filename, mode='wb', encoding='utf-8') as crawled_wf,\
#         codecs.open(word_content, mode='wb', encoding='utf-8') as content_wf:
#         count = 0
#         for word in search_word_list:
#             count += 1
#             search_word = urllib.quote(word)
#             url = 'http://cmtj.cidu.net/log3/file/%s.htm'%search_word
#             try:
#                 html = urllib2.urlopen(url, timeout=15).read().decode('gbk')
#             except:
#                 try:
#                     html = urllib2.urlopen(url, timeout=15).read().decode('gbk')
#                 except:
#                     try:
#                         html = urllib2.urlopen(url, timeout=15).read().decode('gbk')
#                     except:
#                         failed_wf.write(urllib.unquote(url).decode('utf-8')+'\n')
#                         continue
#             familyname_word_content_set = set([item+'\n' for item in html.split()])
#             content_wf.writelines(familyname_word_content_set)
#             crawled_wf.write(urllib.unquote(url).decode('utf-8')+'\n')
#             print count
def search_one_word():
    word = urllib.quote('谈')
    url = 'http://cmtj.cidu.net/log3/file/%s.htm'%word
    html = urllib2.urlopen(url).read().decode('gbk')
    print html
    print html.split()[:2]
# search_one_word()
def filter_familyname_content():
    filename = os.path.join(PATH, 'out', 'familyname_content')
    name_content = os.path.join(PATH, 'out', 'name_content')
    with codecs.open(filename, encoding='utf-8') as f,\
    codecs.open(name_content, mode='wb', encoding='utf-8') as wf:
        word_set = set(f.readlines())
        wf.writelines(word_set)

# filter_familyname_content()