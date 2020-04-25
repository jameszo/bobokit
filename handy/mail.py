import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate  
from email import encoders 
from email.header import Header 
import poplib

class Email:

    def __init__(self):
        self.msg = MIMEMultipart()
        self.msg['Date'] = formatdate(localtime=True)
        self.sender = None
        self.receivers = []
        self.to = []
        self.cc = []

    def set_sender(self, sender):
        self.sender = sender

    def add_receivers(self, receivers):
        self.receivers += receivers

    def set_subject(self, subject):
        self.msg['Subject'] = Header(subject, 'utf-8')

    def add_from(self, fr):
        self.msg['From'] = fr

    def add_to(self, to):
        self.to = self.to + [x for x in to]
        self.msg['To'] = COMMASPACE.join(self._to)

    def add_cc(self, cc):
        self.cc = self.cc + [x for x in cc]
        self.msg['Cc'] = COMMASPACE.join(self.cc)

    def set_content(self, text):
        self.msg.attach(MIMEText(text, 'plain', "utf-8"))

    def add_attach(self, file_path):
        att = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="' + os.path.basename(file_path) + '"'
        self.msg.attach(att)

    def send(self, smtp_server, passwd):
        smtp = smtplib.SMTP(smtp_server)
        smtp.debuglevel=1
        smtp.login(self.sender, passwd)
        smtp.sendmail(self.sender, self.receivers, self.msg.as_string())
        smtp.close()

def mailbox(pop3_server, user, passwd, order):
    server = poplib.POP3(pop3_server)
    print(server.getwelcome())
    server.user(user)
    server.pass_(passwd)
    print('Messages: %s. Size: %s' % server.stat())

    def mails():
        resp, mails, octets = server.list()
        index = len(mails)
        for i in range(len(mails))[::order]:
            resp, lines, octets = server.retr(i)
            msg_content = '\r\n'.join(lines)
            msg = Parser().parsestr(msg_content)
            yield msg

    def quit():
        server.quit()

    return mails, quit

def get_latest_email(pop3_server, user, passwd, rm):
    mails, quit = mailbox(pop3_server, user, passwd, -1)
    msg = next(mails)
    quit()
    return msg

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def print_msg(msg, indent=0):
    if msg is None or msg.strip() == '':
        return None
    charset = guess_charset(msg)
    if charset is None:
        charset = ''
    indent *= 4
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = value.decode(charset)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % (' ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % (' ' * indent, n))
            print('%s--------------------' % (' '  * indent))
            print_msg(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % (' ' * indent, content))
        else:
            #Treat it as attachment. 
            print('%sAttachment: %s' % (' ' * indent, content_type))


