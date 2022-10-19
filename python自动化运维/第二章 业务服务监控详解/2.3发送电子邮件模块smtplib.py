import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from  email.mime.image import MIMEImage


HOST="smtp.qq.com" #定义smtp主机

FROM = "1xxxx@qq.com" #定义邮件收件人
TO = "lxxxxxxxx@163.com" #定义邮件发件人
def text_mime():
    SUBJECT = "Test email from Python"  # 定义邮件主题
    content = "python 脚本发送测试邮件！！！ \n\n\n\n From：aaa" #邮件内容
    msg = MIMEText(content)
    msg["Subject"] = SUBJECT
    msg["From"] = FROM
    msg["To"] = TO

    BODY = msg.as_string()
    print(BODY)

    try:
        server = smtplib.SMTP_SSL(HOST,465) #创建一个SMTP（）对象
        # server.connect(HOST,25)#通过connect方法连接smtp主机
        # server.starttls() #启动安全传输模式
        server.login(FROM,"sxxxxxxxxxxx") #邮箱账号登录校验,注意这里的密码并不一定为邮箱登录密码，像163邮箱需要在设置里开启SMTP，并使用里面的授权码进行登录
        server.sendmail(FROM, TO, BODY) #邮件发送
        server.quit() #断开smtp连接
        print("发送成功 To:"+TO)
    except Exception as e:
        print("发送失败：%s" %e)
def multi_mime():
    content = '<table width="600" border="0" cellspacing="0" cellpadding="4"> <tr bgcolor="#CECFAD" height="20"duokan-code-cn">：14px"><td colspan=2>*官网性能数据 <a href="monitor.domain.com">更多>></a></td> </tr> <tr bgcolor="#EFEBDE" height="100"duokan-code-cn">： 13px"> <td> <img src="cid：io"></td><td> <img src="cid：key_hit"></td> </tr> <tr bgcolor="#EFEBDE" height="100"duokan-code-cn">： 13px"> <td> <img src="cid：men"></td><td> <img src="cid：swap"></td> </tr> </table>'
    SUBJECT = u"业务性能数据报表"  # 定义邮件主题
    msg = MIMEMultipart('related')#创建MIMEMultipart对象，采用 related定义内嵌资源 #的邮件体
    msgtext = MIMEText(content,"html","utf-8")#创建一个MIMEText对象，HTML元素包括表格 <table>及图片<img> #<img>标签的src属性是通过 Content-ID来引用的
    msg.attach(msgtext)#MIMEMultipart对象附加MIMEText的内容
    msg.attach(add_img(src=r"C:\Users\sysadmin\Pictures\Camera Roll\2.jpg",imgid="io"))
    msg.attach(add_img(src=r"C:\Users\sysadmin\Pictures\Camera Roll\2.jpg",imgid="key_hit"))
    msg.attach(add_img(src=r"C:\Users\sysadmin\Pictures\Camera Roll\2.jpg",imgid="men"))
    msg.attach(add_img(src=r"C:\Users\sysadmin\Pictures\Camera Roll\2.jpg",imgid="swap"))
    msg['From']=FROM
    msg["To"] = TO
    msg["Subject"] = SUBJECT

    BODY = msg.as_string()
    print(BODY)
    try:
        server = smtplib.SMTP_SSL(HOST,465)
        server.login(FROM,"xxxxxxxxxxxx")
        server.sendmail(from_addr=FROM,to_addrs=TO,msg=BODY)
        server.quit()
        print("邮件发送成功 TO： "+TO)
    except Exception as e:
        print("发送失败: "+str(e))

def add_img(src,imgid):
    fp = open(src, 'rb')  # 打开文件
    msgimg = MIMEImage(fp.read())  # 创建MIMEImage对象，读取 图片内容并作为参数
    fp.close()  # 关闭文件
    msgimg.add_header('Content-ID', imgid)  # 指定图片文件的 Content-ID ，标签src用到
    return msgimg
if __name__ == '__main__':
    multi_mime()