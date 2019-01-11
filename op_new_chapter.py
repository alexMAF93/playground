#!/usr/local/bin/python3


import urllib.request # we need the source of the page
from bs4 import BeautifulSoup as BS # BS is used to parse the html file
import re # searching for patterns
import os
from email.mime.text import MIMEText
import smtplib # when a new chapter comes up, an email will be sent
from useful_functions import get_credentials_for_email as get_creds # custom function to get the credentials for the email account


def send_email():
    send_to = 'mitroi.alex93@gmail.com'
    MESSAGE = """
New {} Chapter
Chapter {} - {}
Published date: {}

You can read it here: https://readms.net{}
""".format(manga_name, chapter_number, chapter, published_date, chapter_link) 
    msg = MIMEText(MESSAGE)
    msg["Subject"] = "New manga chapter"
    msg["From"] = "Alex"
    msg["To"] = "Alex"
    ACCOUNT = get_creds('/home/alex/parole/send_email.txt')[0]
    PASSWORD = get_creds('/home/alex/parole/send_email.txt')[1].replace('\n', '')

    t = smtplib.SMTP("smtp.gmail.com", 587)
    t.ehlo()
    t.starttls()
    t.login(ACCOUNT, PASSWORD)
    t.sendmail(ACCOUNT, send_to, msg.as_string())
    t.quit()


# the latest chapter's date will be kept in a file in 
# order to compare it with the one retrieved
# every time the script runs
FILE = '/var/tmp/one_piece_chapter.txt'


url = 'https://readms.net/' # the link of the manga site
hdr = {'User-Agent':'Mozilla/5.0'} # we need to use a header because we get a 403 HTTP error
request = urllib.request.Request(url, headers = hdr) 
page = urllib.request.urlopen(request) # getting the page
soup = BS(page, 'html.parser') # we parse this page as a html file


# getting the latest link with One Piece
links_in_page = soup.find_all('a') # all <a> tags in the page 


for link in str(links_in_page).split(','): # going through each link
    if re.match('.*/r/one_piece.*', link): # if it matches the one for One Piece
        link_op = link.strip() # we keep the first result only, since it's the latest
        break


# this is how the links are formatted: date, manga name, chapter number and the title of the chapter
# everything between ( ) is a group and can be retrieved
link_format = '<a href="/r/one_piece.*><span class="pull-right">(.*)</span>(.*)<strong>(.*)</strong><em>(.*)'
link_search = re.search(link_format, link_op, re.IGNORECASE)
if link_search:
    published_date = link_search.group(1)
    manga_name = link_search.group(2).title().strip()
    chapter_number = link_search.group(3)
    chapter = link_search.group(4)


# formatting the link again to add it easily in the message
link_format2 = '<a href="(.*)"><.*'
link_search2 = re.search(link_format2, link_op, re.IGNORECASE)
if link_search2:
    chapter_link = link_search2.group(1)
    

if os.path.isfile(FILE):
    with open(FILE, 'r') as f:
        last_published_date = f.read()
    if last_published_date != published_date:
        with open(FILE, 'w') as f:
            f.write(published_date)
        send_email()        
else:
    with open(FILE, 'w') as f:
        f.write(published_date)    
    send_email()
