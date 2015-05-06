#! /usr/bin/python

import requests, bs4, urllib, os

def getSizes(baseURL):

   res = requests.get(baseURL)
   res.raise_for_status()
   chubbiesSoup = bs4.BeautifulSoup(res.text)

   type(chubbiesSoup)

   titleList = []

   urlList = []

   sizeList = []

   soldOutList = []
   
   title = chubbiesSoup.select('.product-title')

   urlBlock = chubbiesSoup.find_all("div",{"class":"details"})

   for line in title:
      titleList.append(line.get_text(" | ", strip=True))

   for line in urlBlock:
      for row in line.find_all('a'):
         urlList.append('http://www.chubbiesshorts.com' + row['href'])
   
   for line in urlList:
      rez = requests.get(line)
      rez.raise_for_status()
      soup = bs4.BeautifulSoup(rez.text)

      soldOut = soup.find_all("label", {"class":"btn sold-out"})
      
      sizeBlock = soup.find_all("label", {"class":"btn"})

      list1 = []

      list2 = []
     
      for line in sizeBlock:
         list1.append(line.get_text(),)
      
      for line in soldOut:
         list2.append(line.get_text(),)
      
      for x, y in zip(list1, list2):
         if x == y:
            list1.remove(x)
      
      for line in list1:
         sizeList.append(line)

   for line in sizeList:
      print line
      
     



getSizes('http://www.chubbiesshorts.com/collections/the-originals/')
