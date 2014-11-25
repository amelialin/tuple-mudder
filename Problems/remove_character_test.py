from remove_character import remove_character

def test_remove_character():
	assert remove_character("a", "apple") == "pple"
	assert remove_character("e", "apple") == "appl"	
	assert remove_character("a", "apple, with a bite") == "pple, with  bite"
	assert remove_character(",", "apple, with a bite") == "apple with a bite"

	# what is the 'assert' test I would write for throwing an error?