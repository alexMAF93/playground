#!/usr/bin/env python3


import urllib.request, re, sys
from datetime import datetime
from bs4 import BeautifulSoup as BS
from external_IP import send_email
from external_IP import write_to_file


def get_manga(manga_name): # gets the first link that matches the words specified
    url = 'https://readms.net/'
    hdr = {'User-Agent':'Mozilla/5.0'} # we need to use a header because we get a 403 HTTP error
    request = urllib.request.Request(url, headers = hdr)
    page = urllib.request.urlopen(request)
    soup = BS(page, 'html.parser')
    links_in_page = soup.find_all('a') # all <a> tags in the page
    for link in str(links_in_page).split(','):
        if re.match('.*/r/{}.*'.format(manga_name), link, re.IGNORECASE):
            link_manga = link.strip()  # we keep the first result only, since it's the latest
            return link_manga
    else:
        return False


def parse_link(link_manga): # gets the name, chapter and the date from the link
    output = "Cannot find anything..."
    link_regex = '<a href="/r/.*right">(.*)</span>(.*</i>)*(.*)<strong>(.*)</strong>.*<em>(.*)</em></a>'
    if link_manga:
        link_search = re.search(link_regex, link_manga, re.IGNORECASE)
        if link_search:
            published_date = link_search.group(1)
            manga = link_search.group(3)
            chapter = link_search.group(4)
            title = link_search.group(5)
            output = "{}, {} - {}; Released {}".format(manga.strip(), chapter, title, published_date)
    else:
        output = "Nothing found"
    return output


def check_if_email_was_sent(file_path, result):
    REGEX = re.compile(".*{}.*".format(result))
    with open(file_path) as f:
        content = f.readlines()
    for line in content:
        if re.search(REGEX, line):
            return True
    return False


def main():
    file_path = '/var/tmp/manga.log'
    now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    if len(sys.argv) > 1:
        manga_name = sys.argv[1:]
        result = parse_link(get_manga(' '.join(manga_name).replace(' ', '_')))
        # print(result)
        if 'Today' in result and not check_if_email_was_sent(file_path, result):
            send_email(text_message=result,
                       subject='New {} chapter'.format(' '.join(manga_name).title())
        )
            write_to_file(file_path,
                     "{}: New {} chapter {} Email sent\n".format(now, ' '.join(manga_name).title(), result),
                     'a+')
        else:
            write_to_file(file_path,
                     "{}: No new {} chapter found.\n".format(now,  ' '.join(manga_name).title()),
                     "a+")
    else:
        print('You must specify the name of the manga')


if __name__ == "__main__":
    main()
