# -*- coding: UTF-8 -*-

# author:   James Zo
# email:    bobobonet@hotmail.com

import ftplib


def ftp_upload(host, port, username, password, local_file, remote_file):
    bufsize = 1024
    fp = open(local_file, 'rb')
    f = ftplib.FTP()
    f.connect(host, port)
    f.login(username, password)
    f.set_pasv(False)
    f.storbinary('STOR ' + remote_file, fp, bufsize)
    fp.close()
