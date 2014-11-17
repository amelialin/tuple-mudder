from sys import argv

script, user_name, user_age = argv
prompt = 'Tell me here: '

print "Hi %s, I'm the %s script." % (user_name, script)
print "You're %s, and I'd like to ask you a few questions." % user_age
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %s computer. Nice.
""" % (likes, lives, computer)