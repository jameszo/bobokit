# -*- coding: UTF-8 -*-

# author:   James Zo
# email:    james_email@sina.cn

from py.io.file import *
from py.io.mysql import *
import json
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import logging

logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='/Users/James/code/run/words_rdb_collector.log',
                filemode='w+')


logging.info("Running words_rdb_collector...")


poetry_db = None
fail_count = 0

def toStr(v):
    if isinstance(v, (list, tuple)):
        s = ''
        for i in v:
            si = str(i).strip()
            if si == '':
                continue
            s = s + si
        return s
    else:
        return v

def insertArticle(poetry):
    sql = "insert into poetry_db.t_article(title, author, time, content, created, updated) values('%s', '%s', '%s', '%s', now(), now())" %  (toStr(poetry["poetry_title"]), toStr(poetry["poetry_author"]), toStr(poetry["poetry_time"]), toStr(poetry["poetry_content"])) 
    return poetry_db.execute(sql)

def judge_pure_english(keyword):
    return all(ord(c) < 128 for c in keyword)

def insertArticleWords(article_id, poetry_words):
    pw = ''
    for w in poetry_words:
        pw = pw + w + ";"
    sql = "insert into poetry_db.t_article_words(article_id, words, created, updated) values(%d, '%s', now(), now())" %  (article_id, pw)
    return poetry_db.execute(sql)


def insertWord(poetry_words, article_id):
    insert_sql = "insert into poetry_db.t_word(word, article_ids, created, updated)  values('%s', '%s', now(), now())"
    update_sql = "update poetry_db.t_word set article_ids='%s' where word='%s'"
    check_sql = "select id, article_ids from poetry_db.t_word where word='%s'"
    for w in poetry_words:
        cr = poetry_db.query_res(check_sql % w)
        if len(cr) > 0:
            article_ids = json.loads(cr[0]["article_ids"])
            id_dict = {}
            for id in article_ids:
                id_dict[id]=1

            article_ids = []
            for k in id_dict.keys():
                article_ids.append(k)

            poetry_db.execute(update_sql % (json.dumps(article_ids), w))
        else:
            article_ids = [article_id]
            poetry_db.execute(insert_sql % (w, json.dumps(article_ids)))



def deal_poetry(poetry_str):
    global fail_count
    try:
        poetry = json.loads(poetry_str, encoding='utf-8', strict=False)
        poetry_words = []
        pws = jieba.cut(poetry_str, cut_all=True)
        for w in pws:
            w = w.strip()
            if w == '':
                continue
            if judge_pure_english(w):
                continue
            poetry_words.append(w)

        article_id = insertArticle(poetry)
        insertArticleWords(article_id, poetry_words)
        insertWord(poetry_words, article_id)
        print poetry_str
    except BaseException as e:
        fail_count += 1
        logging.exception(e)
        #logging.error(poetry_str)



if __name__ == '__main__':
    poetry_db=Mysql('localhost', 'root', 'ijlkm,')
    File.traverse_path_file('/Volumes/iserv-data/data/gushici', deal_poetry)
    poetry_db.close()
    logging.info("Failed with: " + str(fail_count))
