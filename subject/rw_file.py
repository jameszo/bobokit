# -*- coding: UTF-8 -*-

# author:   James Zo
# email:    james_email@sina.cn

import os
import codecs
import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

def traverse_path_line(path, deal):
    file_list = os.listdir(path)
    for f in file_list:
        filepath = os.path.join(path, f)
        if os.path.isdir(filepath):
            self._traverse_path_count(filepath)
        else:
            with open(filepath) as fo:
                for line in fo:
                    deal(line)

def traverse_path_file(path, deal):
    file_list = os.listdir(path)
    for f in file_list:
        filepath = os.path.join(path, f)
        if os.path.isdir(filepath):
            self._traverse_path_count(filepath)
        else:
            with open(filepath) as fo:
                deal(fo.read())

def copyForWindows(self):
    copy_file = open(self.path + os.path.sep + self.shortname + "_win"  + self.extension, 'w')
    index_src = self.fo.tell()
    self.fo.seek(0)
    line = self.fo.readline()
    while line:
        copy_file.write(codecs.BOM_UTF8)
        copy_file.write(line.encode('utf-8'))
        copy_file.flush()
        line = self.fo.readline()
    self.fo.seek(index_src)

class BaseFile:
    def __init__(self, file_path, access_mode='a'):
        self.fo = open(file_path, access_mode)
        (path, file_name) = os.path.split(file_path);  
        (shortname, extension) = os.path.splitext(file_name);  
        self.file_path = file_path
        self.path = path
        self.file_name = file_name
        self.shortname = shortname
        self.extension = extension

    def write_line(self, line):
        line = line + "\r\n"
        self.fo.write(line)
        self.fo.flush()

    def getAllContent(self):
        str = '';
        contents = self.fo.readlines()
        for line in contents:
            str = str + "\r\n" + line
        return str

    def close(self):
        self.fo.flush()
        self.fo.close()

