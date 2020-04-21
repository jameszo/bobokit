#!/usr/bin/env python3

import json
import datetime
import re

def combine_seqmap(key, sp1, sp2):
    seqmap = []
    for s1 in sp1:
        for s2 in sp2:
            if s2[key] == s1[key]:
                seqmap = seqmap + [dict(s2, **s1)]
    return seqmap

def json_dump(data):
    class DateEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime.datetime):
                return obj.strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(obj, date):
                return obj.strftime('%Y-%m-%d')
            else:
                return json.JSONEncoder.default(self, obj)
    
    return json.dumps(data, cls=DateEncoder)

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
