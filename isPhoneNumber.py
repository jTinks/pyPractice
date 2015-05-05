#!/usr/bin/python

import re

def isPhoneNumber(text):

   if len(text) != 12:
      return False
   for i in range(0,3):
      if not text[i].isdigit():
         return False
   if text[3] != '-':
      return False
   for i in range(4,7):
      if not text[i].isdigit():
         return False
   if text[7] != '-':
      return False
   for i in range(8,12):
      if not text[i].isdigit():
         return False
   return True


print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

print ""

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
   chunk = message[i:i+12]
   if isPhoneNumber(chunk):
      print('Phone number found: ' + chunk)
print('Done')

print ""

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-555-4525')

if mo == None:
   print 'No phone numbers here.'
else:
   print mo.group()









