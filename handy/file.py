#!/usr/bin/env python3

import os
import codecs
import sys

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

