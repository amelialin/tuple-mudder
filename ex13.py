from sys import argv

# sys is an example of a "library", or "module"

script, first, second, third = argv

# argv is the "argument variable". This line "unpacks" argv and says, "Take whatever is in argv, unpack it, and assign it to all the variables on the left (script, first, second, third) in order."

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
# The script is called: ex13.py
# Your first variable is: first
# Your second variable is: 2nd
# Your third variable is: 3rd

# run this program like: python ex13.py first 2nd 3rd

# note: to copy text from Powershell, highlight and hit Enter. Or, click the Powershell icon at top left and select Edit > Copy.