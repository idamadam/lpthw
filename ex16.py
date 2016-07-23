from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# The 'w' is to open the file in write mode
target = open(filename, 'w')

# Truncating is not needed because the 'w' mode truncates any file that exists.
# print "Truncating the file. Goodbye!"
# target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

write_string = ("%s \n%s \n%s") % (line1, line2, line3)
target.write(write_string)

print "And finally, we close it."
target.close()

# The file has to be opened again after closing it.
target = open(filename, 'r')

print "And we open it again"
print target.read()

target.close()
