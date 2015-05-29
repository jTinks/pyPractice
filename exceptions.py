
#print "any number divided by zero is", 7/0

print ""

try:
    print "any number divided by zero is", 7/0

except ZeroDivisionError:
    print "Not possible to divide by zero."
