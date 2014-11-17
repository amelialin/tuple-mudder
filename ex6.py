x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# This line's %r will exactly reproduce what came after the x = sign, with the quotation marks reversed.
print "I said: %r." % x
# I said: 'There are 10 types of people.'.

# This line's %s will be replaced with the exact string represented by y, substituting in the variable values.
print "I also said: '%s'." % y
# I also said: 'Those who know binary and those who don't.'.

hilarious = "False"
# This line's %r builds in a variable to be printed directly inside the string, in this case, the answer to the question.
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
# Isn't that joke so funny?! 'False'

# the difference between %s and %r:
# >>> d = datetime.date.today()
# >>> str(d)
# '2011-05-14'
# >>> repr(d)
# 'datetime.date(2011, 5, 14)'
# %r is the *string* representation of what you would ask python to evaluate in order to get back the value of d.
#
# In this case, using %r with 'hilarious' will give the result 'False', with single quotes, while %s will give the result False, with no quotation marks:

joke_evaluation2 = "Isn't that joke so funny?! %s"
print joke_evaluation2 % hilarious
# Isn't that joke so funny?! False

w = "This is the left side of..."
e = "a string with a right side."

# This line puts strings right next to each other almost as if they were added (+)
print w + e
