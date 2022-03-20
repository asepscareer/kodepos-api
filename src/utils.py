from requests import get
from bs4 import BeautifulSoup

_baseurl_ = 'https://carikodepos.com/daerah'

def url_daerah() -> list:
  page = get(_baseurl_)
  data = []
  soup = BeautifulSoup(page.text, 'lxml')
  table = soup.find_all('td')
  for i in table:
    nama = i.find('a')['href'].strip().split('/')[-2]
    data.append(nama)
  return data

def total_page(url):
  page = get(url)
  soup = BeautifulSoup(page.text, 'lxml')
  total = soup.find('a', class_ = 'last')['href'].strip().split('/')[-2]
  return int(total)

