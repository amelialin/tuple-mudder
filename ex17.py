from sys import argv
from os.path import exists # returns True if a file exists, based on its name, False if not

script, from_file, to_file = argv

# sys is an example of a "library", or "module". argv is the "argument variable". This line "unpacks" argv and says, "Take whatever is in argv, unpack it, and assign it to all the variables on the left (script, first, second, third) in order."

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
# indata = open(from_file).read()
# indata = in_file.read()

# print "The input file is %d bytes long" % len(indata)

# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

# out_file = open(to_file, 'w').write(indata)
# open(to_file, 'w').write(indata)
# out_file.write(indata)

open(to_file, 'w').write(open(from_file).read())

print "All right, all done."

# out_file.close()
# in_file.close()