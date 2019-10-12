# -*- coding: UTF-8 -*-

#author: James Zo
#email: james_email@sina.cn

import MySQLdb

from py.db import *

class Mysql(DB):

    def __init__(self, host, user, passwd, port=3306):
        self._conn = MySQLdb.connect(
                host=host,
                port = port,
                user=user,
                passwd=passwd,
                charset="utf8"
                )

