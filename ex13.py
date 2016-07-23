# How to import modules in Python.
# We are importing the argv method from the sys module
# argv holds all the arguments that are passed to the python program
from sys import argv

# This line unpacks all of the arguments passed to the script in order.
# E.g. python ex13.py first 2nd 3rd becomes
# script = ex13.py, first = first, second = 2nd & third = 3rd.
script, first, second, third = argv

input_var = raw_input("What's the input var?")

# Print the argv values
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your input value is:", input_var
