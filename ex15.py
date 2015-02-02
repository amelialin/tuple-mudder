from sys import argv, exit

if len(argv) != 2:
	print "Usage: ex15.py <filename>"
	exit(1)

# exit is a function that exits python and stops running the script. an parameter (also known as argument) of 0 for exit is a success, anything else counts as a failure.

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

# things like .read are called functions, methods, or "commands", as Zed calls them.

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# close files
txt.close()
txt_again.close()