# -*- coding: UTF-8 -*-

import MySQLdb
import abc

class DB(metaclass=abc.ABCMeta):

    def __init__(self, host, username, passwd, port):
        self.conn = self.connect(host, username, passwd, port)

    @abc.abstractmethod
    def connect(host, username, passwd, port):pass

    def execute(self, sql):
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback();
        cur.close()

    def query_res(self, sql, params):
        cur = self._conn.cursor()
        cur.execute(sql, params)
        index = cur.description
        rows = []
        cur_set = cur.fetchall();
        if cur_set is None:
            return rows
        for res in cur_set:
            row = {}
            for i in range(len(index)):
                row[index[i][0]] = res[i]
            rows.append(row) 
        self._conn.commit()
        cur.close()
        return rows

    def close(self):
        self.conn.close()

    def __init__(self, host, user, passwd, sql):
        Mysql.__init__(self, host, user, passwd)
        self._header = []
        self._description = self.view(sql)
        for i in range(len(self._description)):
            self._header += [{'name':self._description[i][0]}]

    def next_row(self):
        cur_one = self._cur.fetchone()
        if not cur_one:
            return None
        return self.trans_row_res(self._description, cur_one)

    def view(self, sql):
        self._cur = self._conn.cursor()
        self._cur.execute(sql)
        return self._cur.description

    def _write_header(self):
        if not self._header:
            raise Exception("Get no table header.")
        line = ''
        for h in self._header:
            if h.has_key('title'):
                hc = h['title']
            elif h.has_key('name'):
                hc = h['name']
            else:
                continue
            line = line + str(hc) + ','
        line = line[:-1]
        self.write_line(line)


    def _write_row(self):
        row = self.next_row()
        if not row:
            return None
        line_str = ''
        for h in self._header:
            name = str(h['name'])
            if row.has_key(name):
                cell = str(row[name]).replace(',', '、')
            else:
                cell = ''
            line_str = line_str + cell + ','
        line_str = line_str[:-1]
        self.write_line(line_str)
        return row


class Mysql(DB):

    def __init__(self, host, user, passwd, port=3306):
        self._conn = MySQLdb.connect(
                host=host,
                port = port,
                user=user,
                passwd=passwd,
                charset="utf8"
                )
