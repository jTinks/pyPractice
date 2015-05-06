#!/usr/bin/python


import smtplib

sender = 'jtink010@yahoo.com'
receivers = ['jtink010@gmail.com']

message = """From: Chubbies Alert <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: Chubbies Size Update

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
