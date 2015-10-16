# imports the argv library from the sys module
from sys import argv

# sets our command line arguments
script, filename = argv

# print "What file are you trying to read?"
# filename = raw_input("> ")

txt = open(filename)
print txt.read()
txt.close()

# instantiates txt as our file object
txt = open(filename, 'a+')
txt.write("I am another line!\n ")
txt.close()

# prints some text
print "Here's your file %r:" % filename

txt = open(filename)
print txt.read()
txt.close()

# asks for a different file
# print "Type the filename again:"
# fileAgain = raw_input("> ")
#
# # instantiates txt as our file object
# txtAgain = open(fileAgain)
#
# print txtAgain.read()
