# Print message
print "Let's practice everything."
# Print message with single quotes with escape characters, backslashes, new lines and tabs.
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tab.'

# Define poem with multi-line text variable with escape characters.
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nore comprehend passion from intuition
and requires an explanataion
\n\t\twhere there is none.
"""

# Print poem using variable
print "---------------------"
print poem
print "---------------------"

# Define 5 as a variable with maths operations.
five = 10 - 2 + 3 - 6
# Print 5 with the variable defined.
print "This should be five: %s" % five

# Define function of secret_formula with arg "started" and return jelly_beans, jars, crates
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates


start_point = 10000
# Define variables with returned numbers from the secret_formula function.
beans, jars, crates = secret_formula(start_point)

# Print out strings with numerals from defined variables.
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
