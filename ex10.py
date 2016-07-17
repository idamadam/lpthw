tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n \t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# format strings are used as a variable.
# The raw format prints things as literals, the double quotes get replicated in the string formatter.
# The %s format takes out the double quotes and prints them as is.

format = """
"%r" '%s' %s
"""

print format % ("foo", "bar", "baz")
