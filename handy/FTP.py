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
            print "开始接收服务器上的文件..."
            fp = open(localpath.decode('gbk'), 'wb') #以写模式在本地打开文件
            ftp.retrbinary('RETR ' + remotepath,fp.write,bufsize) #接收服务器上文件并写入本地文件
            logging.debug("读取远程地址为%s" % remotepath.decode("utf8").encode("gbk"))
            logging.debug("%s下载成功路径为: %s" %(Zname, localpath))
            print "%s下载成功路径为: %s" %(Zname, localpath)
            fp.close()
        except Exception, e:
            print e
            logging.debug("%s下载失败关闭文件,退出FTP服务器" %Zname)
            print "下载失败"
            os.remove(localpath)
        finally:
            ftp.quit() #退出ftp服务器

    def close(self):
        pass
