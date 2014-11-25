# this one is like your scripts with argv
def print_two(*args): # this DEFINES a function 'print-two'. *args is similar to argv, you'll use it to pack/unpack your arguments. The * says to take all the arguments and stick them in 'args' as a list.
	arg1, arg2 = args # here's where you can use *args to 'unpack' your arguments
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this:
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Amelia", "Lin")
print_two_again("Amelia", "Lin")
print_one("First!")
print_none()