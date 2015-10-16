from sys import argv
from os.path import exists

script, fromFile, toFile = argv


#we could do these two on one line too, how?
inFile = open(fromFile, 'r')
indata = inFile.read()

print "The input file is %d bytes long" % len(indata)

print "Are you sure you want to copy %s to %s? RETURN to continue, CTRL-C to abort." % (fromFile, toFile)
raw_input()
print "Copying File"

outFile = open(toFile, 'w')
outFile.write(indata)

print "Alright, all done."

outFile.close()
inFile.close()
