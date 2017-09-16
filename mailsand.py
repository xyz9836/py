# -*- coding: utf-8 -*-
import urllib
import urllib2
import requests
from threading import Thread
import smtplib
from email.header import Header
from email.mime.text import MIMEText

def send_offline():
    test_data = {'text':'云监工报告','desp':'有设备状态异常'}
    test_data_urlencode = urllib.urlencode(test_data)
    requrl = "https://sc.ftqq.com/SCU10361T0a2416cf6a6ca09da852bf223a588c2f59776131cef7d.send"
    req = urllib2.Request(url = requrl,data =test_data_urlencode)


# 验证邮箱格式
def validateEmail(email):
    import re
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return 1
    return 0


# 异步发送邮件
def send_async_email(email, config_info):
    Thread(target=send_email, args=[email, config_info]).start()


# 发送邮件
def send_email(email, config_info):
    SERVER = config_info['master_mail_smtp']  # 邮箱smtp服务器
    PORT = 25  # 邮箱smtp端口
    USERNAME = config_info['master_mail_address']  # smtp账号
    PASSWORD = config_info['master_mail_password']  # smtp授权密码
    FROM = USERNAME
    TO = email.get('to')
    SUBJECT = email.get('subject')
    TEXT = email.get('text')

    msg = MIMEText(TEXT.encode('utf-8'), 'html', 'utf-8')
    msg['From'] = FROM
    msg['To'] = TO
    msg['Subject'] = Header(SUBJECT, 'utf-8')

    try:
        smtp = smtplib.SMTP(SERVER, PORT)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(USERNAME, PASSWORD)
        smtp.sendmail(FROM, TO, msg.as_string())
        smtp.quit()
        return True
    except Exception as e:
        print(e)
        return False
