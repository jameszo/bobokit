# -*- coding: UTF-8 -*-

# author:   James Zo
# email:    james_email@sina.cn


import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate  
from email import encoders 
from email.header import Header 


class Email:

    title = None

    def __init__(self):
        self._msg = MIMEMultipart()
        self._msg['Date'] = formatdate(localtime=True)
        self._to = []
        self._cc = []
        self._text = ''

    def add_to(self, *to):
        self._to = self._to + [x for x in to]
        self._msg['To'] = COMMASPACE.join(self._to)

    def add_cc(self, *cc):
        self._cc = self._cc + [x for x in cc]
        self._msg['Cc'] = COMMASPACE.join(self._cc)

    def set_sender(self, sender, passwd):
        self._sender = sender
        self._passwd = passwd
        self._msg['From'] = sender

    def set_subject(self, subject):
        self._msg['Subject'] = Header(subject, 'utf-8')

    def add_content(self, text):
        self._text = self._text + text
        self._msg.attach(MIMEText(self._text, 'plain', "utf-8"))

    def clear_text(self):
        self._text = ''
        self._msg.attach(MIMEText(self._text, 'plain', "utf-8"))

    def add_file(self, file_path):
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(file_path, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % Header(os.path.basename(file_path), 'utf-8'))
        self._msg.attach(part)

    def send(self, smtp_server):
        smtp = smtplib.SMTP(smtp_server)
        smtp.debuglevel=1
        smtp.login(self._sender, self._passwd)
        smtp.sendmail(self._sender, self._to + self._cc, self._msg.as_string())
        smtp.close()
