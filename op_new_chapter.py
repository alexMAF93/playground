#!/usr/bin/env python3


import urllib.request, re, sys
from bs4 import BeautifulSoup as BS


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
        print('Cannot find a link for the name you specified')


def parse_link(link_manga): # gets the name, chapter and the date from the link
    output = "Cannot find anything..."
    link_regex = '<a href="/r/.*right">(.*)</span>(.*</i>)*(.*)<strong>(.*)</strong>.*<em>(.*)</em></a>'
    link_search = re.search(link_regex, link_manga, re.IGNORECASE)
    if link_search:
        published_date = link_search.group(1)
        manga = link_search.group(3)
        chapter = link_search.group(4)
        title = link_search.group(5)
        output = """
{}, {} - {}
Released {}
    """.format(manga.strip(), chapter, title, published_date)
    return output


def main():
    if len(sys.argv) > 1:
        manga_name = sys.argv[1:]
        print(parse_link(get_manga(' '.join(manga_name).replace(' ', '_'))))
    else:
        print('You must specify the name of the manga')


if __name__ == "__main__":
    main()
