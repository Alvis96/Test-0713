import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "dh346846@gmail.com"
receiver = ["p42106@gmail.com","dh346846@gmail.com"]
for i in receiver:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = i
    header = Header("To my Baby Reindeer","utf-8")
    msg["Subject"] = header.encode()

    body = "This email send from my Iphone"
    #mbody = MIMEText(body)
    #msg.attach(mbody)
    msg.attach(MIMEText(body))
    ssl_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:  #smtp.gmail.com--跟google連線的網址,465--port
        server.login(sender,"pdej wjxt ucpi ybup")
        server.sendmail(sender,i,msg.as_string())
    print("success send email")