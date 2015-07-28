# Put 10 into the string
x = "There are %d types of people." % 10
# set variable binary to the string binary
binary = "binary"
# set variable do_not to the string don't
do_not = "don't"
# set y to the string with the variables filled in
y = "Those who know %s and those who %s." % (binary, do_not)

# Print out the variable x
print x
# Print out the variable y
print y

# print x with some text before in a format used for debugging
print "I said: %r." % x
# print y with some text before in a format used for display strings to users
print "I also said: '%s'." % y

# set the variable hilarious to true
hilarious = True
# create a string with a format character
joke_evaluation = "Isn't that joke so funny?! %r"

# evaluate the value of hilarious into the string joke_evaluation
print joke_evaluation % hilarious

# create two string variables
w = "This is the left side of ..."
e = "a string with a right side"

# concatenate those two strings together
print w + e