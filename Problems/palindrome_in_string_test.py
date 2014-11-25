from palindrome_in_string import palindrome_in_string

def test_palindrome_in_string():
	assert palindrome_in_string("a")
	assert palindrome_in_string("aa")
	assert palindrome_in_string("abba")
	assert palindrome_in_string("aba")
	assert palindrome_in_string("a a")

	assert not palindrome_in_string("apple")