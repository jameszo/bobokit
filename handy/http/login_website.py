#!/usr/bin/env python3

import os
import time
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from hand.image import captcha

def login_github(username, passwd):
    session = requests.Session()
    r_login = session.get('https://github.com/login')
    s_login = BeautifulSoup(r_login.text, features='lxml')
    authenticity_token =  s_login.find(name='input', attrs={'name': 'authenticity_token'}).get('value')
    cookies = r_login.cookies.get_dict()
    r_login.close()

    form_data = {
        "authenticity_token": authenticity_token,
        "utf8": "",
        "commit": "Sign in",
        "login": username,
        'password': passwd
    }
    r_session = session.post('https://github.com/session', data=form_data)
    cookies.update(r_session.cookies.get_dict())
    return session, cookies

def login_zhihu(email, passwd):
    """
    Just an example, not tested.
    """
    session = requests.Session()

    i1 = session.get(
        url='https://www.zhihu.com/#signin',
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
        }
    )
    soup1 = BeautifulSoup(i1.text, 'lxml')
    xsrf_tag = soup1.find(name='input', attrs={'name': '_xsrf'})
    xsrf = xsrf_tag.get('value')

    current_time = time.time()
    i2 = session.get(
        url='https://www.zhihu.com/captcha.gif',
        params={'r': current_time, 'type': 'login'},
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
        })
    with open('zhihu.gif', 'wb') as f:
        f.write(i2.content)

    captcha = captcha.getstr('zhihu.gif')
    os.remove('zhihu.gif')
    form_data = {
        "_xsrf": xsrf,
        'password': passwd,
        "captcha": captcha,
        'email': email
    }
    i3 = session.post(
        url='https://www.zhihu.com/login/email',
        data=form_data,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
        }
    )

    return session
