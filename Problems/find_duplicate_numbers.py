# Given an array of size N containing integers < M, with N >> M (e.g. there are 
# duplicates), find the duplicates.

# Time complexity O(n). Including elements in a set is O(1). For loop is O(n).

def find_duplicate_numbers(array):
    """Returns a set of duplicated elements from array of integers"""
    unique_values = set(array)
    return set([i for i in array 
                if not i in unique_values or unique_values.remove(i)])

def find_duplicates(array):
    """Returns a set of duplicated elements from array"""
    duplicates = set()
    seen = set()
    for i in array:
      if i not in seen:
        seen.add(i)
      else:
        duplicates.add(i)
    return duplicates


if __name__ == '__main__':
    from sys import argv
    print find_duplicate_numbers(argv[1:])
