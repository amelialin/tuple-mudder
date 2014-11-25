# Write a function to check if a string is a palindrome.

# old version
def palindrome(word):
	length = len(word) - 1
	i = 0
	while i <= length / 2:
		if word[i] != word[length - i]:
			return False
		i += 1
	return True

# new version
def palindrome(word):
	for i in range(0, len(word) / 2):
		if word[i] != word[-(i + 1)]:
			return False
	return True

if __name__ == '__main__':
 	from sys import argv
 	script, word = argv
 	print palindrome(word)

# ==PSEUDOCODE==
# if the word has an even num of chars
	# pair up the chars until word[i] where i = length/2
# if the word has an ODD num of chars
	# pair up the chars until word[i] where i = (length - 1)/2

# However, in practice bc of the way math is
# calculated in Python, you should just be able 
# to take length/2 for both cases; e.g. 5/2 = 2
