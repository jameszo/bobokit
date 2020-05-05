#!/usr/bin/env python3

import unittest
import os
import shutil

TEST_DIR = "./testtmpdir"

class TestFile(unittest.TestCase):

    def setUp(self):
        if os.path.exists(TEST_DIR):
            self.fail("Test dir already exists.")
        os.makedirs(TEST_DIR);

    def tearDown(self):
        shutil.rmtree(TEST_DIR)

