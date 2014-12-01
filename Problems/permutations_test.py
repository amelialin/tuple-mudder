from permutations import permutations

def test_permutations():
    assert permutations("12") == ["12", "21"]
    assert permutations("123") == ['123', '132', '213', '231', '312', '321']
    assert permutations("ab ") == ['ab ', 'a b', 'ba ', 'b a', ' ab', ' ba']