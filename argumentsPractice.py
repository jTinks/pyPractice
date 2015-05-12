#!/usr/bin/python

import sys


if len(sys.argv) < 3:
   sys.exit('Please enter the URL for the shorts and the size you are looking for.')

if len(sys.argv) > 3:
   sys.exit('Only two arguments are allowed.' '\n'
   'Please enter the URL for the shorts and the size you are looking for.')

print sys.argv[1]

print sys.argv[2]



