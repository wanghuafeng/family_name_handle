#encoding:utf-8
import re
from tone2Pinyin import ConvertToneNumbersPinyin

args = "Zhào Qián Sūn Lǐ Zhōu Wú Zhèng Wáng"

# lineOut = ConvertToneNumbersPinyin(args)
# print lineOut

s = u"""Zhào Qián Sūn Lǐ Zhōu Wú Zhèng Wáng
赵 钱 孙 李 周 吴 郑 王
Féng Chén Chǔ Wèi Jiǎng Shěn Hán Yáng冯 陈 褚 卫 蒋 沈 韩 杨
Zhū Qin Yoú Xǔ Hé Lǚ Shi Zhāng
朱 秦 尤 许 何 吕 施 张"""

def convert_to_pinyin_num():
    words_pinyin_dic = {}
    pattern = re.compile(u"[\u4e00-\u9fa5]+")
    param_list = s.split()
    flag_point = 0
    for param in param_list:
        match = pattern.match(param)
        if not match:
            param = param.encode("utf-8")
            lineOut = ConvertToneNumbersPinyin(param)
            key_words = param_list[flag_point+8]
            print key_words
            value_pinyin_num = lineOut + "\n"
            words_pinyin_dic[key_words] = value_pinyin_num
        flag_point += 1
    return words_pinyin_dic
# convert_to_pinyin_num()
def write_file():
    words_pinyin_dic = convert_to_pinyin_num()
    with open("words_pinyin_num.txt",mode="a") as f:
        for key in words_pinyin_dic:
            print key,words_pinyin_dic[key]
            com_str ="\t".join((key,words_pinyin_dic[key]))
            print com_str
            f.write(com_str.encode("utf-8"))
# write_file()
def read_file():
    import codecs
    # fileObj = codecs.open("family_name_words_pin.txt",mode="wb",encoding="utf-8")
    with codecs.open("words_pinyin_num.txt",encoding="utf-8") as f:
        pattern = re.compile("[1-9]")
        for line in f.readlines():
            match = pattern.search(line)
            if match:
                print pattern.sub(" ",line)
                trim_num = pattern.sub(" ",line)
                # fileObj.write(trim_num)
    # fileObj.close()
# read_file()
def re_sub_fun():
    '''正则中的替换操作'''
    import codecs
    with codecs.open("words_pinyin_num.txt",encoding="utf-8") as f:
        for line in f.readlines():
            print re.sub("\d"," ",line,count=1)

# read_file()
def convert_pinyin_lower():
    '''字符串操作，大小写转换'''
    import os,codecs
    fileObj = open("multi_family_name.txt",mode="wb")
    with codecs.open("family_name_words_pin.txt") as f:
        for line in f.readlines():
            lower_line = line.lower()
            fileObj.write(lower_line)
    fileObj.close()
# convert_pinyin_lower()
def test_listdir_fun():
    '''测试listdir，函数，其他的类似遍历方法还有glob，以及os.walk()'''
    import os
    print os.listdir(".")

def str_find_fun():
    '''find函数，字符串中进行查找，查找失败则返回-1，
    所以不能直接用if str.find('*')来判断是否查询失败'''
    s = "谁了"
    flag = s.find("天")
    print flag
    if s.find("天") != -1:
        print "yes"
    # if s.find("天"):
    #     print "yes"
# str_find_fun()
def check_mulitfamilyname_in_omit():
    '''确定姓氏准确发音与高频词不同，即姓氏部分可能会被错误标音的字'''
    import codecs
    omit_words_set = set()
    multi_intersection_dic = {}
    high_freq_pinyin_dic = {}
    with codecs.open("data/omit_check_words.txt",encoding="utf-8") as f:
        for line in f.readlines():
            omit_words_set.add(line.strip())
    print len(omit_words_set)
    with codecs.open("data/multi_family_name.txt",encoding="utf-8") as f:
        for line in f.readlines():
            splited_line = line.strip().split("\t")
            if  splited_line[0] in omit_words_set:
                multi_intersection_dic[splited_line[0]] = splited_line[1]
    with codecs.open("data/high_frequence_single_word.txt",encoding="utf-16") as f:
        for line in f.readlines():
            splited_line = line.strip().split("\t")
            high_freq_pinyin_dic[splited_line[0]] = splited_line[1]
    i = 0
    temp_list = []
    for (k,v) in multi_intersection_dic.items():
        if (k,v) not in high_freq_pinyin_dic.items():
            i += 1
            com_str = "\t".join((k,v,high_freq_pinyin_dic[k]))
            com_str = com_str + "\n"
            temp_list.append(com_str)
            print k,v,high_freq_pinyin_dic[k]
    print len(temp_list)
    # with codecs.open("omit_not_eq_high_freq.txt",mode="wb",encoding="utf-8") as f:
    #     f.writelines(temp_list)
# check_mulitfamilyname_in_omit()
def gen_multi_pinyin():
    '''获取2,3,4，5,6多音字,且按顺序排列'''
    import os,codecs
    path = r"E:\SVN\chocolate_ime\doc"
    filename = os.path.join(path,"HZout_NoTone.txt")
    word_list = []
    with codecs.open(filename,mode="rb",encoding="utf-16") as f:
        for line in f.readlines():
            splited_line = line.split("\t")
            word_list.append(splited_line[0])
    multi_pinyin_num_dic = {}
    for word in set(word_list):
        multi_pinyin_num_dic[word] = word_list.count(word)#数据量为23721，利用list.count速度相当慢
    com_temp_list = []
    multi_pinyin_num_list = sorted(multi_pinyin_num_dic.items(),key=lambda x:x[1])#按照dic的value值进行排序，sorted返回数组
    for word_repeat_times_tuple  in multi_pinyin_num_list:
        if word_repeat_times_tuple[1] >= 2:
            com_str = "\t".join((word_repeat_times_tuple[0],str(word_repeat_times_tuple[1])))
            com_str = com_str + "\n"
            com_temp_list.append(com_str)
    print len(com_temp_list)
    with codecs.open("multi_repeat_times_sort.txt",mode="a",encoding="utf-8") as f:
        f.writelines(com_temp_list)
# gen_multi_pinyin()

def gen_multi_familyname_dic():
    import codecs
    multi_familyname_dic = {}
    with codecs.open("familyname_not_equal_high_freq.txt",encoding="utf8")as f:
        for line in f.readlines():
            # print len(line.split("\t"))
            splited_line = line.split("\t")
            multi_familyname_dic[splited_line[0]] = splited_line[1]
    print multi_familyname_dic
# gen_multi_familyname_dic()
def get_high_freq():
    '''max函数比较，两个参数，interator,key,对arr中的第三个参数进行比较，然后返回对应的list
    注意，此时若不用float进行转化，则会按字符串进行比较，及"22"小于"4"，这个问题的不是第一次碰到了，
    当慎重才是'''
    arr = [[u'\u90fd', u'du', u'3093398\r\n'], [u'\u90fd', u'dou', u'18953009\r\n']]
    high_word_pinyin_freq_list = max(arr, key=lambda x: float(x[2]))
    print high_word_pinyin_freq_list
#get_high_freq()
