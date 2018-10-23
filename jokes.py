#!/usr/local/bin/python3


from email.mime.text import MIMEText
import smtplib, urllib.request, re


url = "http://www.rinkworks.com/jokes/random.cgi"
joke = urllib.request.urlopen(url).readlines()
check_var = 0
MESSAGE = ""

for i in range(len(joke) - 1):
    if str(joke[i].decode()).startswith('<h2>#'):
        check_var = 1
    if str(joke[i].decode()).startswith('</td>') and check_var == 1:
        break
    
    if check_var == 1:
         MESSAGE += re.sub('</?..?/?>|<img.*/>', '', str(joke[i].decode()))


msg = MIMEText(MESSAGE)
msg["Subject"] = "Esti cel mai tare!!!"
msg["From"] = "alex"
msg["To"] = "andrei"
recipients = ['mitroi.alex93@gmail.com', 'dina.vlad.andrei@gmail.com']


t = smtplib.SMTP("smtp.gmail.com", 587)
t.ehlo()
t.starttls()
t.login("maf.alex93@gmail.com", "parolasmechera")
t.sendmail("maf.alex93@gmail.com", recipients, msg.as_string())
t.quit()
