# -*- coding: UTF-8 -*-

"""
    author:   BoBoBo
    email:    bobobonet@hotmail.com 
"""

import unittest
import os
import shutil

TEST_DIR = "./test_tmp"

class TestFile(unittest.TestCase):


    def setUp(self):
        if os.path.exists(TEST_DIR):
            shutil.rmtree(TEST_DIR)
        os.makedirs(TEST_DIR + "/d1/d11/d111");
        os.makedirs(TEST_DIR + "/d2/d21");
        with open(TEST_DIR + "/f1", 'w') as f1:
            f1.writelines(["f1:1","f1:2"])

    def test_traverse_file(self):
        self.fail("TODO")

