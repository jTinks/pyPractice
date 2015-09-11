#! /usr/bin/python

# A simple calculator that performs the desired operation on 2 numbers.

# define functions

from decimal import *

def add(x, y):
    """This function adds two numbers"""

    return x + y

def subtract(x, y):
    """This function subtracts two numbers"""

    return x - y

def multiply(x, y):
    """This function multiplies two numbers"""

    return x * y

def divide(x, y):
    """This function divies two numbers"""

    return x / y

# list input choices
print 'Select operation'
print '1. Add'
print '2. Subtract'
print '3. Multiply'
print '4. Divide'
print '5. Exit'

while True:

    choice = raw_input('Enter the number of the desired operation:')

    if choice == '1':
        num1 = Decimal(raw_input('Enter the first number:'))
        num2 = Decimal(raw_input('Enter the second number:'))
        print num1, '+', num2, '=', add(num1, num2)
        break

    elif choice == '2':
        num1 = Decimal(raw_input('Enter the first number:'))
        num2 = Decimal(raw_input('Enter the second number:'))
        print num1, '-', num2, '=', subtract(num1, num2)
        break

    elif choice == '3':
        num1 = Decimal(raw_input('Enter the first number:'))
        num2 = Decimal(raw_input('Enter the second number:'))
        print num1, '*', num2, '=', multiply(num1, num2)
        break

    elif choice == '4':
        num1 = Decimal(raw_input('Enter the first number:'))
        num2 = Decimal(raw_input('Enter the second number:'))
        print num1, '/', num2, '=', divide(num1, num2)
        break

    elif choice == '5':
        break

    else:
        print 'invalid input'

print 'Operation complete. Exiting.'
exit()
