#!/usr/local/bin/python3


from email.mime.text import MIMEText
import smtplib, urllib.request, os


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
    OLD_EXTERNAL_IP = EXTERNAL_IP


# comparing the 2 addresses
# and if they're not equal,
# an email will be sent
if EXTERNAL_IP != OLD_EXTERNAL_IP:
    msg = MIMEText(EXTERNAL_IP)
    msg["Subject"] = "The external IP was changed for centos"
    msg["From"] = "centos"
    msg["To"] = "mitroi.alex93@gmail.com"

    t = smtplib.SMTP("smtp.gmail.com", 587)
    t.ehlo()
    t.starttls()
    t.login("maf.alex93@gmail.com", "parolasmechera")
    t.sendmail("maf.alex93@gmail.com", "mitroi.alex93@gmail.com", msg.as_string())
    t.quit()
    with open(output_file, 'w') as write_IP:
        write_IP.write(EXTERNAL_IP)
