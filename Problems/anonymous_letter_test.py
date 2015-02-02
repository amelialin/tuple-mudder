from anonymous_letter_working import anonymous_letter

# why didn't I have to import all the helper functions too?

def test_anonymous_letter():
    assert anonymous_letter("apple box", "apple box chair") == True
    assert anonymous_letter("apple! Box", "Apple, box, chair") == True
    assert anonymous_letter("apple! Box dog", "Apple, box, chair") == False
    assert anonymous_letter("apple! Box dog", "Apple, box, chair Dog") == True
    assert anonymous_letter("apple! Box dog dog", "Apple, box, chair Dog") == False
    assert anonymous_letter("", "empty letter") == True
    assert anonymous_letter("empty magazine", "") == False