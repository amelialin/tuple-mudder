from find_duplicate_numbers_working import find_duplicate_numbers

def test_find_duplicate_numbers():
    assert find_duplicate_numbers([1, 2, 3, 3]) == [3]
    assert find_duplicate_numbers([1, 2, 3, 3, 3, 2]) == [2, 3]
    assert find_duplicate_numbers([3, 1, 2, 3, 3, 3, 2, 1]) == [1, 2, 3]
    assert find_duplicate_numbers([1, 2, 6]) == []
    assert find_duplicate_numbers([1, 20, 30, 30]) == [30]