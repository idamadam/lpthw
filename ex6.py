# Create a string with an input and add that number to it. 
x = "There are %d types of people." % 10
# Create a variable for binary
binary = "binary"
# Create a variable for do_not
do_not = "don't"
# Construct a string with these two variables
y = "Those who know %s and those who %s." % (binary, do_not)

# Display the first sentence.
print x
# Display the second sentence
print y

# Print the raw string of x
print "I said: %r." % x
# Print the normal string for s
print "I also said: '%s'." %y

# Establish that you are not funny
hilarious = False
# Print the raw string about the joke
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious 

w = "This is the left side of..." 
e = "a string with a right side."

print w + e
