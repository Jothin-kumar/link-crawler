from bs4 import BeautifulSoup
from requests import get


def crawl(url, startswith='', endswith=''):
    source_code = get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.startswith(startswith) and href.endswith(endswith):
            yield href