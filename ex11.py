print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# Extra Credit
# The function is raw_input([prompt])
# The prompt can be used as the question without a trailing newline

s = raw_input('--> ')

print s
