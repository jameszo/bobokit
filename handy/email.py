#!/usr/bin/env python3

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate  
from email import encoders 
from email.header import Header 

class Email:

    def __init__(self):
        self.msg = MIMEMultipart()
        self.msg['Date'] = formatdate(localtime=True)
        self.to = []
        self.cc = []

    def add_to(self, to):
        self.to = self.to + [x for x in to]
        self.msg['To'] = COMMASPACE.join(self._to)

    def add_cc(self, cc):
        self.cc = self.cc + [x for x in cc]
        self.msg['Cc'] = COMMASPACE.join(self.cc)

    def set_sender(self, sender):
        self.msg['From'] = sender

    def set_subject(self, subject):
        self.msg['Subject'] = Header(subject, 'utf-8')

    def set_content(self, text):
        self.msg.attach(MIMEText(text, 'plain', "utf-8"))

    def add_attach(self, file_path):
        att = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="' + os.path.basename(file_path) + '"'
        message.attach(att)

    def send(self, smtp_server):
        smtp = smtplib.SMTP(smtp_server)
        smtp.debuglevel=1
        smtp.login(self._sender, self._passwd)
        smtp.sendmail(self._sender, self._to + self._cc, self._msg.as_string())
        smtp.close()
