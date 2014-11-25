# Write a function to find the longest palindrome in a string.

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

def palindrome(word):
	length = len(word) - 1
	i = 0
	while i <= length/2:
		# print i
		if word[i] == word[length-i]:
			# print word[i], "matches", word[length-i]
			pass
		else:
			# print word[i], "does not match", word[length-i]
			return False
		i += 1 # increment position
	return True

def palindrome_in_string(string):
	length_of_string = len(string)
	i = 0 # set counter = 0
	# start with full string, evaluate if palindrome if not, check the 2 substrings that are length-1 long, then 3 substrings that are length-2 long, etc. example:
	j = 0 # cutoff from ends of string
	while j <= i: # CHECK LATER
		substring = string[j:length_of_string-(i-j)]
		if palindrome(substring) == True:
			print substring
			return palindrome(substring)
		else:
			pass
		j += 1
	return False
# if yes at any point, then store that in a variable and return it
# if always no, spit out the last 1-character letter in the string

if __name__ == '__main__':
 	from sys import argv
 	script, string = argv
 	print palindrome_in_string(string)



