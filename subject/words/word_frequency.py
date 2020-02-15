# -*- coding: UTF-8 -*-

import os
import re
from py.io.file import File
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class WordCounter:

    __words={}

    def __init__(self, data_path, output_path, core_word):
        self.__data_path = data_path
        self.__core_word = core_word
        self.__output_path = output_path
        self.__dataset_size = 0

    def count(self):
        File.traverse_path_file(self.__data_path, self.dealWords)
        self.__sort_words()
        return self.__words

    def dealWords(self, content):
        if(content.find(self.__core_word) >= 0):
            self.__dataset_size += 1
            self.__count(content)

    def get_words(self):
        return self.__words

    def __count(self, str):
        ws = jieba.cut(str, cut_all=True)
        tag = {}
        for w in ws:
            w = w.strip()
            m = re.match("[a-z]+", w)
            if(m != None):
                continue
            if(w == '' or w == '[' or w ==']' or w == '{' or w == '}' or w == ',' or w == ':' or w == '一'):
                continue
            print w
            c = 0
            if self.__words.has_key(w):
                c = self.__words[w]
            c+=1
            if(not tag.has_key(w+"_"+str)):
                f = File(self.__output_path + w, 'a+')
                f.write_line(str + '\n\r\n\r\n\r')
                f.close()
                tag[w+"_"+str]=True
            self.__words[w]=c

    def __sort_words(self):
        self.__words = sorted(self.__words.iteritems(), key=lambda d:d[1], reverse = True)

    def get_dataset_size(self):
        return self.__dataset_size;


if __name__ == '__main__':
    output_path = '/Volumes/iserv-data/data/word_count/gushici_new3/'
    counter = WordCounter('/Volumes/iserv-data/data/gushici/', output_path, '峨眉')
    res = counter.count()
    o = File(output_path + 'word_frequency', 'w+');
    cloud_words = File(output_path + 'cloud_words', 'w+');
    size = counter.get_dataset_size()
    o.write_line("该关键词涉及到文章：" + str(size) + "篇")

    for r in res:
        if not isinstance(r,tuple):
            continue
        if len(r) < 2:
            continue
        s = r[0] + " : " + str(r[1])
        ws = r[0] + ";" + str(r[1]) + ";;;;;"
        print s
        o.write_line(s)
        cloud_words.write_line(ws)

    o.close()
    cloud_words.close()
