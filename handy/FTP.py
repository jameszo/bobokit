#!/usr/bin/env python3

import ftplib

class FTPClient(object):

    def __init__(self, host, username, passwd, pasv):
        self.conn = ftplib.FTP()
        self.conn.connect(host, port)
        self.conn.login(username, password)
        self.conn.set_pasv(pasv)
        self.bufsize = 1024
        print(self.conn.getwelcome())

    def upload(self, host, port, username, password, local_file, remote_file):
        fp = open(local_file, 'rb')
        f.storbinary('STOR ' + remote_file, fp, bufsize)
        fp.close()

    def download(self, remotepath, localpath):
        remotepath = os.path.join(remotepath, Zname).encode('utf-8')
        localpath = os.path.join(localpath, Zname).encode("gbk")
        try:
            fp = open(localpath.decode('gbk'), 'wb')
            ftp.retrbinary('RETR ' + remotepath,fp.write,bufsize)
            fp.close()
        except Exception, e:
            os.remove(localpath)
        finally:
            ftp.quit()

    def close(self):
        pass
