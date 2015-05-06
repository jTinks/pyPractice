#! /usr/bin/python

import requests, bs4, urllib, os, smtplib

def getSizes(baseURL):

   res = requests.get(baseURL)
   res.raise_for_status()
   chubbiesSoup = bs4.BeautifulSoup(res.text)

   type(chubbiesSoup)

   titleList = []

   #urlList = ['http://www.chubbiesshorts.com/collections/the-originals/products/the-blutos']

   urlList = []   

   sizeList = []

   soldOutList = []

   outPut = []
   
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

      inStock = []

      outStock = []
     
      for line in sizeBlock:
         inStock.append(line.get_text())
      
      for line in soldOut:
         outStock.append(line.get_text())
      
      for x, y in zip(inStock, outStock):
         if x == y:
            inStock.remove(x)

      sizeList.append('[%s]' % ', '.join(map(str, inStock)))

   if len(titleList) == len(sizeList):
      for x, y, z in zip(titleList, sizeList, urlList):
         outPut.append(x + "  " + y + "  " + z + "\n")
         outPut.append("\n")
   else:
      outPut.append('# of titles does not match # of sizes in lists')

   value = ''.join(outPut)

   return value 
     



theOriginals = getSizes('http://www.chubbiesshorts.com/collections/the-originals/')

theTrunks = getSizes('http://www.chubbiesshorts.com/collections/the-swim-trunks/')


sender = 'jtink010@yahoo.com'
receivers = ['jtink010@gmail.com']

message = """From: Chubbies Alert <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: Chubbies Size Update
""" + theOriginals

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"

