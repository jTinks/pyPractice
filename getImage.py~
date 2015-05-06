#! /usr/bin/python 

import requests, bs4, urllib, os

if not os.path.exists('chubbiesPics/theOriginals'):
   os.makedirs('chubbiesPics/theOriginals')

if not os.path.exists('chubbiesPics/theTrunks'):
   os.makedirs('chubbiesPics/theTrunks')

res1 = requests.get('http://www.chubbiesshorts.com/collections/the-originals/')
res1.raise_for_status()
originalsSoup = bs4.BeautifulSoup(res1.text)

res2 = requests.get('http://www.chubbiesshorts.com/collections/the-swim-trunks/')
res2.raise_for_status()
trunksSoup = bs4.BeautifulSoup(res2.text)

titleO = originalsSoup.select('.product-title')

titleT = trunksSoup.select('.product-title')

imgBlockO = originalsSoup.select('.colleflex')

imgBlockT = trunksSoup.select('.colleflex')

titleListO = []

titleListT =[]

for line in titleO:
   titleListO.append(line.get_text(" | ", strip=True))

for line in titleT:
   titleListT.append(line.get_text(" | ", strip=True))

imgListO = []

imgListT = []


for line in imgBlockO:
   for row in line.find_all('img'):
      imgListO.append('http:' + row['src'])

for line in imgBlockT:
   for row in line.find_all('img'):
      imgListT.append('http:' + row['src'])

for url, title in zip(imgListO, titleListO):
   urllib.urlretrieve(url, os.path.join('chubbiesPics/theOriginals', title + ".jpg"))

for url, title in zip(imgListT, titleListT):
   urllib.urlretrieve(url, os.path.join('chubbiesPics/theTrunks', title + ".jpg"))

