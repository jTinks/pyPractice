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
   smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"
