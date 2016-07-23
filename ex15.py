# Import argv from sys
from sys import argv

# Unpack argument variables
script, filename = argv

# Open the text file and assign it to txt
txt = open(filename)

# Read the txt file and print it out
print "Here's your file %r:" % filename
print txt.read()

# Print the txt file after getting the filename from a raw_input
print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()

file.close(txt)
file.close(txt_again)

# This doesn't work because just the script name has a .py after it.
# Eg this resolves to ex15.py_example.txt
# txt_ezy = open(script+"_example.txt")
# print txt_ezy.read()
