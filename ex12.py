age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

# This accomplishes the same thing as:
# print "How old are you?",
# age = raw_input()
# print "How tall are you?",
# height = raw_input()
# print "How much do you weigh?",
# weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# STUDY DRILLS
# to look up documentation on a python command? function? use:
# python -m pydoc XXXX
# e.g. python -m pydoc raw_input