# Write a function that removes all occurrences of a given character from a string.

# ==PSEUDOCODE==
# maybe check that inputted char is indeed a single character?
# go one char at a time through a string
# if the char does not match, copy it into a second string
# if the char matches, don't copy it into a second string

def remove_character(char, string):
	if len(char) != 1:
		raise ValueError("Please enter a single character only to remove.") # not sure how to best raise an exception?
	length = len(string) - 1 # store length of string
	i = 0
	string_wo_character = "" # create empty string
	while i <= length:
		if string[i] == char: # if the character matches
			pass # don't copy the character
		else:
			string_wo_character += string[i] # append the character
		i += 1 # increment counter
	return string_wo_character

if __name__ == '__main__':
	from sys import argv
	script, char, string = argv
	print remove_character (char, string)