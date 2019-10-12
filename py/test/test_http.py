# -*- coding: UTF-8 -*-

# author:   James Zo
# email:    james_email@sina.cn

import unittest
from py.http import ScriptClient

class TestScriptClient(unittest.TestCase):

    def setUp(self):
        self.example_f = open("./example_http_script_client.yml", 'r')
        self.script = self.example_f.read()
        self.client = ScriptClient(self.script)

    def tearDown(self):
        self.example_f.close()

    def test_do_example(self):
        result = self.client.do("new_user")
        self.assertTrue(result[0], result[1])
        result = self.client.do("get_user_by_uid")
        self.assertTrue(result[0], result[1])

if __name__ == '__main__':
    unittest.main()


