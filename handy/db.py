#!/usr/bin/env python3

import ConfigParser
import abc
import os
import collections
import MySQLdb
from DBUtils.PooledDB import PooledDB

DBconf = collections.namedtuple('DBconf', [
    'host',
    'port',
    'name',
    'user',
    'passwd',
    'mincached',
    'maxcached',
    'maxconnections',
    'maxshared',
    'blocking',
    'maxshared',
    'ping'
    ])

pool = None
pool_lock = 1
conf = None
load_dbconf()

def load_dbconf():
    conf_path = os.environ['handy_conf_file']
    conf = ConfigParser.ConfigParser()
    conf.read(conf_path)

    global conf
    conf = DBconf(
        conf.get('db', 'host'),
        conf.get('db', 'port'),
        conf.get('db', 'name'),
        conf.get('db', 'user'),
        conf.get('db', 'passwd'),
        conf.get('db', 'mincached'),
        conf.get('db', 'maxcached'),
        conf.get('db', 'maxconnections'),
        conf.get('db', 'maxshared'),
        conf.get('db', 'blocking'),
        conf.get('db', 'maxshared'),
        conf.get('db', 'ping')
        )

class DB(metaclass=abc.ABCMeta):

    def __init__(self, pooled=True):
        if pooled:
            global db_pool
            global db_pool_lock
            if not db_pool:
                db_pool_lock.acquire()
                if not db_pool:
                    db_pool = PooledDB(creator=MySQLdb,
                        host=db.host,
                        port=db.port,
                        db=db.name,
                        user=db.user,
                        passwd=db.passwd,
                        mincached=db.mincached,
                        maxcached=db.maxcached,
                        maxconnections=db.maxconnections,
                        maxshared=db.maxshared,
                        blocking=db.blocking,
                        maxshared=db.maxshared,
                        ping=db.ping
                        )
                db_pool_lock.release()
            self.conn = pool.connection() 
        else:
            self.conn = self.connect(host=db.host,
                        port=db.port,
                        db=db.name,
                        user=db.user,
                        passwd=db.passwd
                        )

    @abc.abstractmethod
    def connect(host, user, passwd, port):pass

    def execute(self, sqls):
        cur = self.conn.cursor()
        try:
            for s, p in sqls:
                cur.execute(s, p)
            self.conn.commit()
            res_all = cur.fetchall()
            return self.convert_res(cur.description, res_all)
        except:
            self.conn.rollback()
            return None
        finally:
            cur.close()
            self.conn.close()

    def convert_res(self, description, res_all):
        rows = []
        if res_all is None:
            return rows
        for res in res_all:
            row = {}
            for i in range(len(description)):
                row[description[i][0]] = res[i]
            rows.append(row) 
        return rows

class Mysql(DB):

    def connect(host, user, passwd, port):
        self._conn = MySQLdb.connect(
                host=host,
                port = port,
                user=user,
                passwd=passwd,
                charset="utf8"
                )
