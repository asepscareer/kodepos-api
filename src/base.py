from os import abort
from requests import get
from bs4 import BeautifulSoup
from pandas import read_html, concat, DataFrame, read_csv
from .utils import url_daerah, total_page, _baseurl_

def get_daerah() -> list:
  page = get(_baseurl_)
  data = []
  soup = BeautifulSoup(page.text, 'lxml')
  table = soup.find_all('td')
  for i in table:
    name = i.find('a').text.strip()
    link = i.find('a')['href'].strip().split('/')[-2]
    data.append({
        "Nama" : name,
        "Link": link
        })
  return data

def setup_provinsi():
  list_url = url_daerah()
  for i in list_url:
    tpage = total_page('{}/{}'.format(_baseurl_, i))
    data = []
    for j in range(tpage+1):
      url = 'https://carikodepos.com/daerah/{}/page/{}/'.format(i,j)
      r = get(url)
      res = read_html(r.text)
      data.append(res)

    tail1 = data[len(data)-1][0]
    try:
      tail2 = data[len(data)-1][1]
    except:
      tail2 = DataFrame()
    for k in range(len(data[:-1])):
      data1 = data[k][0].convert_dtypes()
      data2 = data[k][1].convert_dtypes()
      if k == 0:
        df1 = concat([tail1, data1])
        df2 = concat([tail2, data2])
      else:
        df1 = concat([df1, data1])
        df2 = concat([df2, data2])
    df1.reset_index(drop=True, inplace=True)
    df2.reset_index(drop=True, inplace=True)

    cols = {0: 'Propinsi', 1: 'Kota/Kab.', 2: 'Kecamatan', 3: 'Kelurahan', 4: 'Kode Pos'}
    df2 = df2.rename(columns = cols)
    df = concat([df1, df2])
    df.to_csv(f'./data/{i}.csv', index= False)
  return None

def setup_nasional():
  list_data = url_daerah()
  tail_data = read_csv('./data/{}.csv'.format(list_data[-1]))
  for i in range(len(list_data[:-1])):
    df = read_csv('./data/{}.csv'.format(list_data[i]))
    if i == 0:
      data = concat([tail_data, df])
    else:
      data = concat([data, df])
  data.to_csv(f'./data/nasional.csv', index= False)
  return None

def getdata_nasional():
  df = read_csv('./data/nasional.csv')
  data = df.to_dict(orient='records')
  return data

def getdata_provinsi(params:str):
  provinsi = params.lower()
  provinsi = provinsi.replace(' ', '-')
  df = read_csv('./data/{}.csv'.format(provinsi))
  data = df.to_dict(orient='records')
  return data

def get_paginated_list(results, url, start, limit):
  start = int(start)
  limit = int(limit)
  count = len(results)
  if count < start or limit < 0:
    abort(404)
  obj = {}
  obj['start'] = start
  obj['limit'] = limit
  obj['count'] = count
  if start == 1:
    obj['previous'] = ''
  else:
    start_copy = max(1, start - limit)
    limit_copy = start - 1
    obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
  if start + limit > count:
    obj['next'] = ''
  else:
    start_copy = start + limit
    obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
  obj['results'] = results[(start - 1):(start - 1 + limit)]
  return obj