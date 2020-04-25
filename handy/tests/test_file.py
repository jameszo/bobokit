#!/usr/bin/env python3

import unittest
import os
import shutil

TEST_DIR = "./testtmpdir"

class TestFile(unittest.TestCase):

    def setUp(self):
        if os.path.exists(TEST_DIR):
            shutil.rmtree(TEST_DIR)
        os.makedirs(TEST_DIR + "/d1/d11/d111");
        os.makedirs(TEST_DIR + "/d2/d21");
        with open(TEST_DIR + "/f1", 'w') as f1:
            f1.write("f1:1" + os.linesep + "f1:2")
        with open(TEST_DIR + "/d1/d11/f11", 'w') as f1:
            f1.write("f11:1" + os.linesep + "f11:2")

    def tearDown(self):
        shutil.rmtree(TEST_DIR)

    def test_traverse_line(self):
        pass

