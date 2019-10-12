# -*- coding: UTF-8 -*-

# author:   James Zo
# email:    james_email@sina.cn


from py.file import *
from py.mysql import *

class MysqlTable(Mysql, File):

    def __init__(self, host, user, passwd, sql):
        Mysql.__init__(self, host, user, passwd)
        self._header = []
        self._description = self.view(sql)
        for i in range(len(self._description)):
            self._header += [{'name':self._description[i][0]}]

    def get_header(self):
        return self._header

    def next_row(self):
        cur_one = self._cur.fetchone()
        if not cur_one:
            return None
        return self.trans_row_res(self._description, cur_one)

    def view(self, sql):
        self._cur = self._conn.cursor()
        self._cur.execute(sql)
        return self._cur.description

    def close(self):
        self._cur.close()
        self._conn.close()

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

    def _write_content(self):
        while self._write_row() :
            pass

    def write(self, file_full_path):
        File.__init__(self, file_full_path)
        self._write_header()
        self._write_content()

