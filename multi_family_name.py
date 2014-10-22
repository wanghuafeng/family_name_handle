#coding=utf8
import os
import codecs
PATH = r"e:/SVN/chocolate_ime/doc"

BASE_FILE = os.path.join(PATH,"HZout_NoTone.txt")#encoding:utf-16
CIZU_FILE = os.path.join(PATH,"Cizu_komoxo95K.txt")#encoding:gbk
def read_noTone():
    NoTone_set = set()
    multi_pinyin_set = set()
    with codecs.open(BASE_FILE,mode='rb',encoding='utf-16') as f:
        for line in f.readlines():
            splited_line = line.split("\t")
            if splited_line[0] in NoTone_set:
                multi_pinyin_set.add(splited_line[0])     
            NoTone_set.add(splited_line[0])
    print len(multi_pinyin_set),len(NoTone_set)
    return NoTone_set
#read_noTone()
def read_95K():
    cizu_set = set()
    multi_cizu_set = set()
    with codecs.open(CIZU_FILE,encoding="gbk") as f:
        for line in f.readlines():
            splited_line = line.split("\t")
            if splited_line[0] in cizu_set:
                multi_cizu_set.add(splited_line[0])
                # print splited_line[0]
            cizu_set.add(splited_line[0])
    print len(cizu_set),len(multi_cizu_set)
    return cizu_set
# read_95K()
def gen_all_multi_pinyin():
    noTone_set = read_noTone()
    cizu_set = read_95K()
    combined_set = noTone_set.union(cizu_set)
    return combined_set

def gen_mul_family_name():
    combined_set = gen_all_multi_pinyin()
    #fileObj = open("multi_family_name.txt",mode="wb")
    with codecs.open("all_familyname_word_pinyin.txt",encoding="utf-8") as f:
        for line in f.readlines():
            splited_line = line.split("\t")
            # if splited_line[0] in combined_set:
                #fileObj.write(line.encode("utf-8"))
                # print splited_line[0]
    #fileObj.close()
# gen_mul_family_name()
def check_set_efficience():#time consume:0.286000013351
    combined_set = gen_all_multi_pinyin()
    avg = u'得了了'
    if avg in combined_set:
        print 'yes'

#********************set_time_consume_check********************************
def gen_set_cizu():
    cizu_set = set()
    with codecs.open(CIZU_FILE,encoding="gbk") as f:
        for line in f.readlines():
            if line.startswith(";"):
                pass
            else:
                splited_line = line.split("\t")
                cizu_set.add(splited_line[0])
    # print len(cizu_set)
    return cizu_set
def gen_set_word():
    word_set = set()
    with codecs.open(BASE_FILE,encoding="utf-16") as f:
        for line in f.readlines():
            splited_line = line.split("\t")
            word_set.add(splited_line[0])
    # print len(word_set)
    return word_set
def set_combined():
    cizu_set = gen_set_cizu()
    word_set = gen_set_word()
    combined_set = cizu_set.union(word_set)
    print len(combined_set)#206842
    return combined_set
def word_time_check():#0.316999912262,0.31299996376,0.321000099182
    combined_set = set_combined()
    s = u"知不"
    if s in combined_set:
        print 'yes'
# word_time_check()
#********************dic_time_consume_check********************************
def gen_dic_cizu():
    cizu_dic = {}
    with codecs.open(CIZU_FILE,encoding="gbk") as f:
        for line in f.readlines():
            if line.startswith(";"):
                pass
            else:
                splited_line = line.split("\t")
                cizu_dic[splited_line[0]] = splited_line[1]
    # print len(cizu_dic)
    return cizu_dic
def gen_dic_word():
    word_dic = {}
    with codecs.open(BASE_FILE,encoding="utf-16") as f:
        for line in f.readlines():
            if line.startswith(";"):
                pass
            else:
                splited_line = line.split("\t")
                word_dic[splited_line[0]] = splited_line[1]
    # print len(word_dic)
    return word_dic
def dic_combined():
    cizu_dic = gen_dic_cizu()
    word_dic = gen_dic_word()
    cizu_dic.update(word_dic)
    print len(cizu_dic)#206842
    return cizu_dic

def dic_time_check():#0.322000026703,0.327999830246,0.329999923706
    combined_dic = dic_combined()
    s = u"知不"
    if s in combined_dic:
        print 'yes'
# dic_time_check()
#********************list_time_consume_check********************************
def gen_list_cizu():
    cizu_list = []
    with codecs.open(CIZU_FILE,encoding="gbk") as f:
        for line in f.readlines():
            if line.startswith(";"):
                pass
            else:
                splited_line = line.split("\t")
                cizu_list.append(splited_line[0])
    # print len(cizu_list)
    return cizu_list
def gen_list_word():
    word_list = []
    with codecs.open(BASE_FILE,encoding="utf-16") as f:
        for line in f.readlines():
            if line.startswith(";"):
                pass
            else:
                splited_line = line.split("\t")
                word_list.append(splited_line[0])
    # print len(word_list)
    return word_list
def list_combined():
    cizu_list = gen_list_cizu()
    word_list = gen_list_word()
    cizu_list.extend(word_list)
    print len(cizu_list)#210602
    return cizu_list
def list_time_check():#0.240000009537,0.243000030518,0.244999885559
    combined_list = list_combined()
    s = u"知不"
    if s in combined_list:
        print "yes"
# list_time_check()
def time_check(fun):
    import time
    start_time = time.time()
    fun()
    end_time = time.time()
    print end_time - start_time
# time_check(list_time_check)
def find_word_eq_freq():
    word_freq_tuple_set = set()
    multi_word_freq_set = set()
    with codecs.open(BASE_FILE,mode='rb',encoding='utf-16') as f:
        for line in f.readlines():
            splited_line = line.split("\t")
            word_freq_tuple = (splited_line[0],splited_line[2])
            if word_freq_tuple in word_freq_tuple_set:
                eq_word_freq = word_freq_tuple[0] + "\n"
                multi_word_freq_set.add(eq_word_freq)
                print word_freq_tuple[0],word_freq_tuple[1]
            word_freq_tuple_set.add(word_freq_tuple)
    print len(multi_word_freq_set)
    # return multi_word_freq_set
    # with codecs.open("eq_word_freq.txt",mode="wb",encoding="utf-8") as f:
    #     f.writelines(multi_word_freq_set)
# find_word_eq_freq()