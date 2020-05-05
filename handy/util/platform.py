#!/usr/bin/env python3

import os
import codecs
import sys

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

