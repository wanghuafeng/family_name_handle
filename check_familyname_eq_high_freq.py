

def check_mulitfamilyname_in_omit():
    import codecs
    omit_words_set = set()
    multi_intersection_dic = {}
    high_freq_pinyin_dic = {}
    # with codecs.open("data/omit_check_words.txt",encoding="utf-8") as f:
    #     for line in f.readlines():
    #         omit_words_set.add(line.strip())
    # print len(omit_words_set)
    with codecs.open("data/multi_family_name.txt",encoding="utf-8") as f:
        for line in f.readlines():
            splited_line = line.strip().split("\t")
            # if  splited_line[0] in omit_words_set:
            multi_intersection_dic[splited_line[0]] = splited_line[1]
    with codecs.open("data/high_frequence_single_word.txt",encoding="utf-16") as f:
        for line in f.readlines():
            splited_line = line.strip().split("\t")
            high_freq_pinyin_dic[splited_line[0]] = splited_line[1]
    i = 0
    for (k,v) in multi_intersection_dic.items():
        if (k,v) not in high_freq_pinyin_dic.items():
            i += 1
            print k,v,high_freq_pinyin_dic[k]
check_mulitfamilyname_in_omit()