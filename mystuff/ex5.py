myName = 'Zed A. Shaw'
myAge = 35 #not a lie
myHeight = 74 #inches
myWeight = 180 #lbs
myEyes = 'Blue'
myTeeth = 'White'
myHair = 'Brown'

def PoundsToKilos(pounds):
    kilos = pounds * 0.45
    return kilos

def InchesToCentimeters(inches):
    centimeters = inches * 2.54
    return centimeters

print "Let's talk about %s." % myName
print "He's %d inches or %d centimeters tall." % (myHeight, InchesToCentimeters(myHeight))
print "He's %d pounds or %d kilos heavy." % (myWeight, PoundsToKilos(myWeight))
print "He's got %s eyes and %r hair." % (myEyes, myHair)
print "His teeth are usually %s depending on the coffee." % myTeeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (myAge, myHeight, myWeight, myAge + myHeight + myWeight)
