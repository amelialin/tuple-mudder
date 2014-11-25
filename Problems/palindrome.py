# Write a function to check if a string is a palindrome.

# ==PSEUDOCODE==
# if the word has an even num of chars
	# pair up the chars until word[i] where i = length/2
# if the word has an ODD num of chars
	# pair up the chars until word[i] where i = (length - 1)/2

# However, in practice bc of the way math is calculated in Python, you should just be able to take length/2 for both cases; e.g. 5/2 = 2

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

if __name__ == '__main__': # __name__ is a special variable that is set to have the value '__main__' *if* the script is executing as the main function; e.g. you run '$ python palindrome.py'. By adding this line, you are ensuring that the following lines only execute when you want to run the module as a *program*; they will not be run when we just want to *import* our module somewhere else and call the functions ourselves.
 	# KEIR - CORRECT!
 	from sys import argv
 	script, word = argv
 	print palindrome(word)



