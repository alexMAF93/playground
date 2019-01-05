#!/usr/local/bin/python3


from email.mime.text import MIMEText
import smtplib, urllib.request, os
from useful_functions import get_credentials_for_email as get_creds


# getting the current external IP
url = "http://whatismyip.akamai.com"
EXTERNAL_IP = urllib.request.urlopen(url).read().decode()

# getting the old external IP from a file
output_file = '/root/scripts/.external_ip.txt'
if os.path.isfile(output_file):
    with open(output_file, 'r') as read_IP:
        OLD_EXTERNAL_IP = read_IP.read()
# otherwise, the file will be written with
# the external IP
else:
    with open(output_file, 'w') as write_IP:
        write_IP.write(EXTERNAL_IP)
    OLD_EXTERNAL_IP = ""


# comparing the 2 addresses
# and if they're not equal,
# an email will be sent
if EXTERNAL_IP != OLD_EXTERNAL_IP:
    msg = MIMEText(EXTERNAL_IP)
    ACCOUNT = get_creds('/home/alex/parole/send_email.txt')[0]
    PASSWORD = get_creds('/home/alex/parole/send_email.txt')[1].replace('\n', '')
    msg["Subject"] = "The external IP was changed for centos"
    msg["From"] = "centos"
    msg["To"] = "mitroi.alex93@gmail.com"

    t = smtplib.SMTP("smtp.gmail.com", 587)
    t.ehlo()
    t.starttls()
    t.login(ACCOUNT, PASSWORD)
    t.sendmail(ACCOUNT, "mitroi.alex93@gmail.com", msg.as_string())
    t.quit()
    with open(output_file, 'w') as write_IP:
        write_IP.write(EXTERNAL_IP)
