# -*- coding: UTF-8 -*-

"""
    author:   BoBoBo
    email:    bobobonet@hotmail.com 
"""

import os
import codecs
import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

def traverse_file(path, deal):
    for file_path in list(map(os.path.join(path, f), os.listdir(path))):
        if os.path.isdir(file_path):
            self.traverse_path_count(file_path)
        else:
            with open(file_path) as fo:
                deal(fo)

def traverse_line(path, dealline):
    def deal(fo):
        for line in fo:
            dealline(line)

    traverse_file(path, deal)

def make_win32_copy(file_path, copy_path):
    fo = open(file_path, 'r')
    copy_file = open(copy_path, 'w')
    index_src = fo.tell()
    fo.seek(0)
    line = fo.readline()
    while line:
        copy_file.write(codecs.BOM_UTF8)
        copy_file.write(line.encode('utf-8'))
        copy_file.flush()
        line = fo.readline()
    fo.close()

class File:
    def __init__(self, file_path, access_mode='a'):
        self.fo = open(file_path, access_mode)
        (path, file_name) = os.path.split(file_path);  
        (shortname, extension) = os.path.splitext(file_name);  
        self.file_path = file_path
        self.path = path
        self.file_name = file_name
        self.shortname = shortname
        self.extension = extension

    def write_by_line(self, line, flush_now):
        line = line + os.linesep
        self.fo.write(line)
        if flush_now:
            self.fo.flush()

    def flush_file(self):
        self.fo.flush()

    def close(self):
        flush_file()
        self.fo.close()

