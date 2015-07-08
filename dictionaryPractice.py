__author__ = 'jtink'

# Exploring the dictionary data type

brian = {'Age': '25', 'Birthday': 'January 1', 'Height': '6 foot, 4 inches', 'Weight': '210 lbs'}

print ""

#for key, value in jaysen.iteritems():
#    print key, value


print 'What do you want to know about Brian?'
stat = raw_input()
if stat == '':
    exit()

if stat in brian:
    if stat == 'Age':
        print "Brian is", brian[stat], "years old."
    if stat == 'Birthday':
        print "Brian's birthday is on", brian[stat] + "."
    if stat == 'Height':
        print "Brian is", brian[stat], "tall."
    if stat == "Weight":
        print "Brian weighs", brian[stat] + "."
else:
    print 'Something is wrong here'