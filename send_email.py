#!/usr/bin/env python3


from email.mime.text import MIMEText


msg = MIMEText("Test email")
msg["Subject"] = "Testing the email module"
msg["From"] = "centos"
msg["To"] = "mitroi.alex93@gmail.com"


import smtplib


t = smtplib.SMTP("smtp.gmail.com", 587)
t.ehlo()
t.starttls()
t.login("maf.alex93@gmail.com", "hjk678")


t.sendmail("maf.alex93@gmail.com", "mitroi.alex93@gmail.com", msg.as_string())


t.quit()

