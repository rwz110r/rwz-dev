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
    def __config(self, filename):
        # 第二步：准备附件，增加附件，组装邮件内容和标题
        file = filename
        name = os.path.split(file)[-1]
        print('name--------', name)
        # 读取html文件内容
        with open(file, 'rb') as f:
            mail_body = f.read()
            # 组装邮件内容和标题
            msg = MIMEMultipart()
            # 添加附件内容
            att = MIMEText(mail_body, 'plain', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename={}'.format(name)
            msg.attach(att)
            # 添加邮件的文本内容
            content = '自动化测试报告详情，请查收附件'
            msg.attach(MIMEText(content, 'plain', 'utf-8'))

            msg['Subject'] = Header(self.subject, 'utf-8')
            msg['From'] = self.sender
            msg['To'] = self.receiver
            return msg
    def send_email(self,file):
        msg = self.__config(file)
        try:
            smtp =smtplib.SMTP()
            smtp.connect(self.smtpserver)
            smtp.login(self.username,self.password)
            smtp.sendmail(self.sender, self.receiver, msg.as_string())
        except Exception as msg:
            print(f'邮件发送失败，失败原因：{msg}')
        else:
            print('邮件发送成功')
        finally:
            smtp.quit()

if __name__ == '__main__':
    ce = ConfigEmail()
    # ce.send_email(r'D:\code\VIP8InterfaceTest\report\report2021_01_24_14_35_51.html')