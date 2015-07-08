
#print "any number divided by zero is", 7/0

print ""

try:
    print "Any number divided by zero is..."
    print 7/0

except ZeroDivisionError:
    print "It's not possible to divide by zero."
