from palindrome_in_string import palindrome_in_string

def test_palindrome_in_string():
    assert palindrome_in_string("a") == "a"
    assert palindrome_in_string("aa") == "aa"
    assert palindrome_in_string("abba") == "abba"
    assert palindrome_in_string("aba") == "aba"
    assert palindrome_in_string("a a") == "a a"
    assert palindrome_in_string("apple") == "pp"
    assert palindrome_in_string('ab') == "a"
    assert palindrome_in_string('abx') == "a"
    assert palindrome_in_string('abzy') == "a"
    assert palindrome_in_string('abbb') == "bbb"
    assert palindrome_in_string('ameliailemb') == "meliailem"
    assert palindrome_in_string('ameliailemb test') == "meliailem"
    assert palindrome_in_string("abaa cdedc") == "cdedc"