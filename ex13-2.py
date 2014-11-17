from sys import argv

# sys is an example of a "library", or "module"

script, first, second, third, fourth = argv

# argv is the "argument variable". This line "unpacks" argv and says, "Take whatever is in argv, unpack it, and assign it to all the variables on the left (script, first, second, third, fourth) in order."

fifth = raw_input("What about a fifth variable? ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth
print "Your fifth variable is:", fifth
# The script is called: ex13-2.py
# Your first variable is: 1
# Your second variable is: 2
# Your third variable is: 3
# Your fourth variable is: four
# Your fifth variable is: 5

# run this program like: python ex13-2.py 1 2 3 four

# note: to copy text from Powershell, highlight and hit Enter. Or, click the Powershell icon at top left and select Edit > Copy.