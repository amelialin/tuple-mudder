import random
import sys

# NOTE(keir): The below function returns elements in an arbitary order!
def find_duplicate_numbers_list(array):
    """Given a list, returns set of duplicate entries."""
    unique_values = list(set(array))
    duplicates = list(set([i for i in array if not i in unique_values or unique_values.remove(i)]))
    return duplicates

LETTERS = 'ABCDEFGHIJKLMNOPQRSabcdefghijklmnopqrs'
def random_string(length):
  return ''.join(random.choice(LETTERS) for i in range(length))
  

# This test fails on purpose -- it's showing that sets are unordered.
def test_find_duplicate_numbers_list():
  # Try to find a failing case a bunch of times.
  for i in range(1000):
    # Generate a bunch of random words.
    words = [random_string(random.randint(3, 20)) for j in range(100)]

    # Then take the first few and repeat them.
    duplicates = words[:5]
    words_with_duplicates = words + duplicates
    
    # Then shuffle it all so the dupes are in arbitrary places.
    random.shuffle(words_with_duplicates)

    # Previous semantics were expecting sorted results, so sort the duplicates.
    duplicates.sort()

    try:
      computed_duplicates = find_duplicate_numbers_list(words_with_duplicates)
      assert computed_duplicates == duplicates
    except AssertionError:
      print 'Duplicates (actual):\n', computed_duplicates
      print 'Duplicates (expected):\n', duplicates
      raise

if __name__ == '__main__':
  test_find_duplicate_numbers_list()
