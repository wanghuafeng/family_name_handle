__author__ = 'wanghuafeng'
#coding:utf-8
import os
import re
import time
import codecs
import requests
from bs4 import BeautifulSoup

PATH = os.path.dirname(__file__)

def viki_family_name():
    '''从维基百科中抓取所有形式964个'''
    url = r'http://zh.wikipedia.org/zh/%E4%B8%AD%E5%9C%8B%E5%A7%93%E6%B0%8F%E5%88%97%E8%A1%A8'
    html = requests.get(url).text
    soup = BeautifulSoup(html)
    div_level_str = soup.find('div', id='content')
    # print div_level_str
    ul_level_list = div_level_str.find_all('ul')[:-2]
    # print len(ul_level_list[:-2])#23
    total_family_str_list = []
    [total_family_str_list.extend(item.find_all('li')) for item in ul_level_list]
    # print len(total_family_str_list)#969
    # print total_family_str_list[0].text
    family_name_list = [item.text.strip()+'\n' for item in total_family_str_list]
    filename = os.path.join(PATH, 'total_family_name_from_viki_964.txt')
    codecs.open(filename, mode='wb', encoding='utf-8').writelines(family_name_list)
# viki_family_name()

def handle_viki_family_name():
    '''单于（chán yú）中去掉括号（中文标点），词与带声调拼音之间用tab键隔开'''
    filename = os.path.join(PATH, 'total_family_name_from_viki_964.txt')
    com_str_list = []
    with open(filename) as f:
        for line in f.readlines():
            splited_line = line.strip().replace('）', '').split('（')
            word = splited_line[0]
            if len(splited_line) == 2:
                tone_pinyin = splited_line[-1]
                com_str = word+'\t'+tone_pinyin+'\n'
            else:
                com_str = word+'\n'
            com_str_list.append(com_str)
    filename_to_write = os.path.join(PATH, 'total_family_name_from_viki_964_.txt')
    open(filename_to_write, mode='wb').writelines(com_str_list)
# handle_viki_family_name()

def xingshidaquan_family_name():
    '''从姓氏大全网站抓取所有形式1123个，翻页57页'''
    total_family_name_list = []
    for page_index in range(1, 58):
        print page_index
        url = r'http://www.xsdq.org/index.asp?page=%s&'%page_index
        r = requests.get(url)
        html = r.text.encode('ISO-8859-1')
        soup = BeautifulSoup(html)
        div_level_str = soup.find('div', class_='listbox')
        dl_level_list = div_level_str.find_all('dl')
        family_name_list = [item.find('dt').text.strip()+'\n' for item in dl_level_list]
        total_family_name_list.extend(family_name_list)
    filename = os.path.join(PATH, 'total_family_name_from_XSDQ_1123.txt')
    codecs.open(filename, mode='wb', encoding='utf-8').writelines(total_family_name_list)#1123
# xingshidaquan_family_name()

def com_viki_XSDQ():
    '''合并维基百科与姓氏大全上的所有姓氏共1605，没有标音'''
    XSDQ_filename = os.path.join(PATH, 'total_family_name_from_XSDQ_1123.txt')
    viki_filename = os.path.join(PATH, 'total_family_name_from_viki_964.txt')
    with open(viki_filename) as f,\
    open(XSDQ_filename) as Xf:
        viki_set = set([item.strip().split('\t')[0] for item in f.readlines()])
        xsdq_set = set([item.strip() for item in Xf.readlines()])
    print len(viki_set-xsdq_set)
    print len(xsdq_set-viki_set)
    print len(viki_set|xsdq_set)
    com_filename = os.path.join(PATH, 'combine_family_name_1605.txt')
    open(com_filename, mode='wb').writelines([item+'\n' for item in viki_set|xsdq_set])
# com_viki_XSDQ()
