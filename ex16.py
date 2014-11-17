from sys import argv

# tell python the name of the text file to edit. input will look like: "python ex16.py ex16_sample.txt"
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)." # this closes out of python
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') 

# print "Truncating the file. Goodbye!"
# target.truncate() # turns out you don't need this step since using 'open' with 'w' automatically truncates the file. 

# Modes 'r+', 'w+' and 'a+' open the file for updating (reading and writing); note that 'w+' truncates the file. 

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ") # assigns user-inputted values to these variables
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n") # the write command adds the text from the input to the target file.

print "And finally, we close it."
target.close() # gotta remember to close the file!

print "Here's the new file!"

txt = open(filename)
print txt.read()
txt.close()