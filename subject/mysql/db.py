# -*- coding: UTF-8 -*-

#author: James Zo
#email: james_email@sina.cn


class DB:

    def __init__(self):
        self._conn = None

    def execute(self, sql):
        cur = self._conn.cursor()
        cur.execute(sql)
        self._conn.commit()
        cur.close()


    def trans_row_res(self, description, cur_one):
        row = {}
        if {} == cur_one:
            for i in range(len(description)):
                row[description[i][0]] = ''
        else:
            for i in range(len(description)):
                row[description[i][0]] = cur_one[i]
        return row

    
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

    def get_conn(self):
        return self._conn

    def close(self):
        self._conn.close()
