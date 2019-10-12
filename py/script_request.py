# -*- coding: UTF-8 -*-

# author:   James Zo
# email:    james_email@sina.cn

import requests
import re
import yaml
import json
from file import File

class ScriptRequest:

    def __init__(self, script_str):
        self.script = yaml.load(script_str)
        self.script_context = {}

    def doRequest(self, request_name):
        if request_name not in self.script['request']:
            return (False, 'No request named ' + request_name)
        request = self.script['request'][request_name]
        if 'http' == request['type']:
            return self.doHttpRequest(request)
        return (False, 'Not support request type.')

    def doHttpRequest(self, request):
        method = request['method']
        if 'post' == method:
            return self.assertHttpResponse(self.doPost(request), request['response']['assert'])
        elif 'get' == method:
            return self.assertHttpResponse(self.doGet(request), request['response']['assert'])
        return None

    def doGet(self, request):
        cookies = json.loads(request['cookies'])
        r = requests.get(self.getURL(request), cookies=cookies)
        return r

    def doPost(self, request):
        content=request['content']
        if ''  == content:
            j = None
        else:
            content=self.dealPlaceholder(content)
            j = json.loads(content)

        url = self.getURL(request)
        hd = json.loads(request['headers'])

        #r = requests.post(url, json=j, headers=hd, verify=False, cookies=self.cookies)
        cookies = request['cookies']
        if ''  == cookies:
            c = None
        else:
            cookies=self.dealPlaceholder(cookies)
            c = json.loads(cookies)
        r = requests.post(url, data=j,  verify=False, cookies=c)
        return r

    def getURL(self, request):
        return request['type'] + '://' + request['host'] + ':' + str(request['port']) + self.dealPlaceholder(request['path'])

    def assertHttpResponse(self, response, response_assert):
        if response_assert is None:
            return (False, 'No assert script.')

        if 'status' in response_assert:
            if response.status_code != response_assert['status']:
                return (False, 'Status:' + str(response.status_code))

        if 'content' in response_assert:
            match = re.search(response_assert['content'], response.content)
            if not match:
                return (False, 'Content:' + response.content)

        return (True, response.content)

    def dealPlaceholder(self, s):
        matches = re.findall(r'\${[^}]*}', s)
        for m in matches:
            if None == m : break
            v = m[2:-1]
            print("Dealing placeholder: " + v)
            if v.startswith('&'):
                var_name = v[1:]
                holder_value = self.script_context[var_name]
                print "Find holder_value: " + holder_value
                s = s.replace(m, holder_value)
                print "After dealPlaceholder: " + s
        return s
