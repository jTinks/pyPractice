#! /usr/bin/python 

import requests, bs4, urllib, os

res = requests.get('http://www.chubbiesshorts.com/collections/the-originals/')

res.raise_for_status()

chubbiesSoup = bs4.BeautifulSoup(res.text)

type(chubbiesSoup)

details = chubbiesSoup.select('.details')

title = chubbiesSoup.select('.product-title')

price = chubbiesSoup.select('small')

linkBlock = chubbiesSoup.find_all("div",{"class":"details"})

urlList = []

for line in linkBlock:
   for row in line.find_all('a'):
      urlList.append(row['href'])

detailsList = []

for line in details:
   detailsList.append(line.get_text(" | ", strip=True))

titleList = []

for line in title:
   titleList.append(line.get_text(" | ", strip=True))


for deet, url in zip(detailsList, urlList):
   print deet + " | " + 'http://www.chubbiesshorts.com' + url

type(title)

type(price)

type(details)

#print title[0].get_text("|", strip=True)

#print details[0].get_text(" | ", strip=True)

#print price[0].get_text("|", strip=True)


#for i in range(len(title)):
#   print title[i].get_text("|", strip=True) + \
#         " - " + price[i].get_text("|", strip=True)

#for i in range(len(details)):
#   print details[i].get_text(" | ", strip=True) + " | " + \
              


