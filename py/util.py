# -*- coding: UTF-8 -*-

# author:   BoBoBo 
# email:    bobobonet@hotmail.com


import ConfigParser
import logging
import logging.config
import json
import datetime

logger = None


def init_cfg:
    cfg = None

    def cfg(cfg_file="conf.properties"):
        if None == cfg:
            cfg = ConfigParser.ConfigParser()
            cfg.read(cfg_file)
            logging.config.fileConfig(cfg_file)
        log_lvl = cfg.get("log", "level")
    if "debug" == log_lvl:
        logger = logging.getLogger("debugr")
    else:
        logger = logging.getLogger("root")
        logger.info("Cfg is read.")

def init_logger(cfg_file="conf.properties"):


def logger():
    global logger
    return logger

def cfg():
    global cfg
    return cfg

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
