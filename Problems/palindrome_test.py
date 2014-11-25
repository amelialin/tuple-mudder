from palindrome import palindrome # the first 'palindrome' is the name of the palindrome.py file, the second 'palindrome' is the name of the function within that file - KEIR - CORRECT

def test_palindrome():
    # Positive cases. These are the cases that are supposed to return True. But what is the output of an "assert"?
    # KEIR - Assert has no output. If the expression is True, then nothing
    # happens. If it is false, then an AssertionException is thrown. Try it by
    # opening an interactive session and typing 'assert 0'
    assert palindrome('a') 
    assert palindrome('aa')
    assert palindrome('aba')
    assert palindrome('elle')
    assert palindrome('amelilema')

    # Negative cases. These are the cases that are supposed to return False.
    assert not palindrome('ab')
    assert not palindrome('abx')
    assert not palindrome('abzy')
    assert not palindrome('abbb')
    assert not palindrome('ameliailemb')

# if you didn't want to use nose, you could also just add this line to the bottom of your test file
# test_palindrome() 