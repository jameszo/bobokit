# -*- coding: UTF-8 -*-

# author:   James Zo
# email:    james_email@sina.cn

import os
import codecs
import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

class File:

    def __init__(self, file_path, access_mode='w+'):
        self._fo = open(file_path, access_mode)
        (path,tempfilename) = os.path.split(file_path);  
        (shortname,extension) = os.path.splitext(tempfilename);  
        self._filepath = file_path
        self._path = path
        self._shortname = shortname
        self._extension = extension

    def write_line(self, line):
        line = line + "\r\n"
        self._fo.write(line)
        self._fo.flush()
        return 1

    @staticmethod
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

    @staticmethod
    def traverse_path_file(path, deal):
        file_list = os.listdir(path)
        for f in file_list:
            filepath = os.path.join(path, f)
            if os.path.isdir(filepath):
                self._traverse_path_count(filepath)
            else:
                with open(filepath) as fo:
                    deal(fo.read())

    def copy_for_windows(self):
        copy_file = open(self._path + os.path.sep + self._shortname + "_win"  + self._extension, 'w')
        index_src = self._fo.tell()
        self._fo.seek(0)
        line = self._fo.readline()
        while line:
            copy_file.write(codecs.BOM_UTF8)
            copy_file.write(line.encode('utf-8'))
            copy_file.flush()
            line = self._fo.readline()
        self._fo.seek(index_src)

    def get_fo(self):
        return self._fo

    def content(self):
        str = '';
        contents = self._fo.readlines()
        for line in contents:
            str = str + line
        return str


    def close(self):
        self._fo.flush()
        self._fo.close()
