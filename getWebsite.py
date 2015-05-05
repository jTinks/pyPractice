#! /usr/bin/python 

import requests, bs4

res = requests.get('http://www.chubbiesshorts.com/collections/the-originals/')

res.raise_for_status()

chubbiesSoup = bs4.BeautifulSoup(res.text)

type(chubbiesSoup)

title = chubbiesSoup.select('.product-title')

details = chubbiesSoup.select('.details')

price = chubbiesSoup.select('small')

linkBlock = chubbiesSoup.find_all("div",{"class":"details"})

for line in linkBlock:
   for row in line.find_all('a'):
      print row['href']

type(title)

type(price)

type(details)

#print title[0].get_text("|", strip=True)

#print details[0].get_text(" | ", strip=True)

#print price[0].get_text("|", strip=True)


#for i in range(len(title)):
#   print title[i].get_text("|", strip=True) + \
#         " - " + price[i].get_text("|", strip=True)

for i in range(len(details)):
   for line in linkBlock:
      for row in line.find_all('a'):
         print details[i].get_text(" | ", strip=True) + " | " + \
               row['href']

