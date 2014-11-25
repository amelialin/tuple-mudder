from sys import argv

script, input_file = argv

def print_all(f): # prints contents of a file?
	print f.read()

def rewind(f):
	f.seek(0) # move pointer to beginning of file?

def print_a_line(line_count, f):
	print line_count, f.readline(), # prints out the current line_count

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file) # prints everything

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file) # print line 1

current_line += 1
print_a_line(current_line, current_file) # print line 2

current_line += 1
print_a_line(current_line, current_file) # print line 3