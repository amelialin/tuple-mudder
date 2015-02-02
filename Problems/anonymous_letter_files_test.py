from anonymous_letter_files import anonymous_letter_files

# why didn't I have to import all the helper functions too?

def test_anonymous_letter_files():
    assert anonymous_letter_files("anonymous_letter_test1.txt", "anonymous_letter_test2.txt") == True
    assert anonymous_letter_files("anonymous_letter_test3.txt", "anonymous_letter_test4.txt") == False