from find_missing_number import *

def test_find_missing_number_explicit():
    """Tests with explicit input."""
    assert find_missing_number([1, 2, 4]) == 3
    assert find_missing_number([23, 9, 7, 6, 22, 2, 20, 15, 19, 1, 11, 18, 4, 21, 8, 3, 12, 16, 17, 5, 13, 10]) == 14

def test_find_missing_number_random():
    """Tests with generated input."""
    for i in range(1000):
        array, missing_number = generate_random_array()
        assert find_missing_number(array) == missing_number