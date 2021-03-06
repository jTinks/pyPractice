#! /usr/bin/python

# Find out if a specific size for a pair of Chubbies is in stock. 

import requests, bs4, urllib, os, smtplib, sys

def getSizes(baseURL, size):

   res = requests.get(baseURL)
   res.raise_for_status()
   chubbiesSoup = bs4.BeautifulSoup(res.text)

   type(chubbiesSoup)

   inStock = ''

   soldOutList = []
   
   title = chubbiesSoup.find_all("h1",{"class":"main"})
   title[0].a.decompose()
   title[0].a.decompose()
   title = title[0].get_text(" | ", strip=True)
   
   soldOut = chubbiesSoup.find_all("label", {"class":"btn sold-out"})
   for line in soldOut:
      soldOutList.append(line.get_text("|", strip=True))
   
   if size not in soldOutList:
      inStock = 'True'
   else:
      inStock = 'False'

   if inStock == 'True':
      sender = ['jtink010@yahoo.com']
      receivers = ['jtink010@gmail.com']
      
      message = """From: Chubbies Alert 
                
                """ + 'Size %s is in stock' %size + '\n' + baseURL
      try:
         smtpObj = smtplib.SMTP('localhost')
         smtpObj.sendmail(sender, receivers, message)         
         print "Successfully sent email"
      except SMTPException:
         print "Error: unable to send email"

   else:
      print size + ' is out of stock.'


getSizes(sys.argv[1], sys.argv[2])

#theShorts = getSizes('http://www.chubbiesshorts.com/collections/the-originals/products/the-blutos', 'XL')


