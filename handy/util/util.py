#!/usr/bin/env python3

import json
import datetime
import re
from collections import deque
from functools import wraps
import time
from contextlib import contextmanager

def dedupe(items, key=None):
    check = set()
    for item in items:
        val = item if key is None else key(item)
        if not val in check:
            yield val
            check.add(val)

def search_with_history(lines, pattern, history=5):
    pre_lines=deque(maxlen=5)
    for line in lines:
        if pattern in line:
            yeild line, pre_lines
        pre_lines.append(line)

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

def deal_placeholder(self, s):
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

def timefunc(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} cost: {}', func.__module__, func.__name__, end-start)
        return r
    return wrapper

@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{} cost: {}', label, end - start)
