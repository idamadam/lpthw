formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
		"I had this thing.",
		"That you coud type up right.",
		"But it didn't sign.",
		"So I said goodnight"
		)
