#!/usr/bin/env python3


import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import os
import pickle
import sys
from datetime import datetime


def get_password(filepath, account):
    with open(filepath, 'rb') as f:
        return pickle.load(f)[account]


def send_email(text_message, subject="Notification from Raspberry PI"):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "maf.alex93@gmail.com"
    password = get_password('/home/pi/.passwds', sender_email)
    receiver_email = "mitroi.alex93@gmail.com"
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = "Raspberry PI"
    message["To"] = "mitroi.alex93@gmail.com"
    text = MIMEText(text_message, "plain")
    message.attach(text)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


def get_external_IP():
    r = requests.get("http://whatismyip.akamai.com")
    if r.status_code == 200:
        return r.text
    return ""


def read_from_file(filepath):
    if os.path.isfile(filepath):
        with open(filepath) as f:
            file_content = f.readlines()
            if len(file_content) == 1:
                return file_content[0].replace('\n', '')
    return ""


def write_to_file(filepath, text, writing_mode='w'):
    with open(filepath, writing_mode) as f:
        f.write(text)
    

if __name__ == "__main__":
    filepath = "/tmp/external_IP.txt"
    current_ip = get_external_IP()
    old_ip = read_from_file(filepath)
    now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    if not current_ip:
        write_to_file('/tmp/external_ip_log.txt', 
                    "{}: The external IP cannot be retrieved.\n".format(now),
                    "a+"
        )    
    if not old_ip:
        write_to_file('/tmp/external_ip_log.txt',
                    "{}: Cannot retrieve the IP from {}.\n".format(now, filepath),
                    "a+"
        )

    if current_ip != old_ip and current_ip != "":
        message = "New external IP: {}".format(current_ip)
        send_email(message)
        write_to_file('/tmp/external_ip_log.txt',
                    "{}: {}; Old IP: {};Action: Mail sent!\n".format(now, message, old_ip),
                    "a+"
        )
    elif old_ip and current_ip:
        write_to_file('/tmp/external_ip_log.txt',
                    "{}: Nothing changed - {} = {}\n".format(now, old_ip, current_ip),
                    "a+"
        )
    write_to_file(filepath, current_ip)

