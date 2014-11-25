# Write a function to find the longest palindrome in a string.

from palindrome import palindrome

def palindrome_in_string(string):
	length_of_string = len(string)
	for i in range(0, length_of_string):
		for j in range(0, i + 1):
			substring = string[j:length_of_string - (i - j)]
			if palindrome(substring) == True:
				return substring

if __name__ == '__main__':
 	from sys import argv
 	script, string = argv
 	print palindrome_in_string(string)

# ==PSEUDOCODE==
# set counter = 0
# start with full string, evaluate if palindrome if not, check the 2 substrings that are length-1 long, then 3 substrings that are length-2 long, etc. example:
	# for i = 0, check string from string[0] to string[length]
	# for i = 1
	# 	check string from string[0] to string[length - 1]
	# 	check string from string[1] to string[length]
	# for i = 2
	# 	check string from string[0] to string[length-2]
	# 	check string from string[1] to string[length-1]
	# 	check string from string[2] to string[length]
# if yes at any point, then store that in a variable and return it
# if always no, spit out the last 1-character letter in the string

# def palindrome_in_string(string):
# 	length_of_string = len(string)
# 	print "length of string:", length_of_string
# 	for i in range(0, length_of_string):
# 		print "i", i
# 		for j in range(0, i + 1): # CHECK LATER
# 			print "j", j
# 			substring = string[j:length_of_string - (i - j)]
# 			print "Currently checking:", substring
# 			if palindrome(substring) == True:
# 				print "Palindrome!", substring
# 				return substring

