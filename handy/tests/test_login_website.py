#!/usr/bin/env python3

import unittest
from handy.http.login_website import *
import os


class TestLoginWebsite(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip('Have been tested.')
    def test_github(self):
        username = os.environ['test_login_github_username']
        passwd = os.environ['test_login_github_passwd']
        session, cookies = login_github(username, passwd)

        r_repo = session.get('https://github.com/settings/repositories', cookies=cookies)
        s_repo = BeautifulSoup(r_repo.text, features='lxml')
        mr1s = s_repo.find_all(name='a', attrs={"class": "mr-1"})
        for mr1 in mr1s:
            self.assertTrue(mr1.text.find(username) >= 0)
