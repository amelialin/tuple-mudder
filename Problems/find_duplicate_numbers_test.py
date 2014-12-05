from find_duplicate_numbers import find_duplicate_numbers

def test_find_duplicate_numbers():
    assert find_duplicate_numbers([1, 2, 3, 3]) == set([3])
    assert find_duplicate_numbers([1, 2, 3, 3, 3, 2]) == set([3, 2])
    assert find_duplicate_numbers([3, 1, 2, 3, 3, 3, 2, 1]) == set([1, 2, 3])
    assert find_duplicate_numbers([1, 2, 6]) == set([])
    assert find_duplicate_numbers([1, 20, 30, 30]) == set([30])