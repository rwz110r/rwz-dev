import  smtplib,os,time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

class ConfigEmail():
    def __init__(self):
        # 发送邮箱
        self.sender = 'rwz0804@163.com'
        # 接收邮箱
        self.receiver = '394314321@qq.com'
        # 发送邮件主题
        t = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        self.subject = '自动化测试结果'+t
        # 发送邮件服务器
        self.smtpserver = 'smtp.163.com'
        # 发送邮箱用户/密码
        self.username = 'rwz0804'
        self.password = 'r1w9z92rwz..'