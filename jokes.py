#!/usr/local/bin/python3


from email.mime.text import MIMEText
import smtplib, urllib.request, re, sys


def check_if_email(list_of_emails):
    check = 0
    for email in list_of_emails:
        if not '@' in str(email):
            check = 0
            break
        else:
            check+=1
    if check == 0:
        return False
    else:
        return True


if len(sys.argv) < 2:
    print('You must provide at least an email address as argument')
    sys.exit(7)
elif not check_if_email(sys.argv[1:]):
    print('Please write email addresses!')
    sys.exit(7)
else:
    print('A joke will be sent to these email addresses:')
    for email in sys.argv[1:]:
        print(email)


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
msg["To"] = "everyone"
recipients = sys.argv[1:]


t = smtplib.SMTP("smtp.gmail.com", 587)
t.ehlo()
t.starttls()
t.login("maf.alex93@gmail.com", "parolasmechera")
t.sendmail("maf.alex93@gmail.com", recipients, msg.as_string())
t.quit()
