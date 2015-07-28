# create a string full of formatting characters
formatter = "%r %r %r %r"

# print numbers
print formatter % (1, 2, 3, 4)
# print strings
print formatter % ("one", "two", "three", "four")
# print booleans
print formatter % (True, False, False, True)
# print string of format characters
print formatter % (formatter, formatter, formatter, formatter)
# print out some strings including one with a single quote
print formatter % (
  "I had this thing.",
  "That you could type up right.",
  "But it didn't sing.",
  "So I said goodnight"
  )