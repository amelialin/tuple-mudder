from palindrome import palindrome

def test_palindrome():
    # Positive cases.
    assert palindrome('a')
    assert palindrome('aa')
    assert palindrome('aba')
    assert palindrome('elle')
    assert palindrome('amelilema')

    # Negative cases.
    assert not palindrome('ab')
    assert not palindrome('abx')
    assert not palindrome('abzy')
    assert not palindrome('abbb')
    assert not palindrome('ameliailemb')
