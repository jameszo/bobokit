# -*- coding: UTF-8 -*-

import requests

def getURLContent(method, url, body):
    if 'post' == method:
        r = requests.post(url, data=j,  verify=False)
    else:
        r = requests.get(url)
    return r

def makeRequestByFile(path):
    return

