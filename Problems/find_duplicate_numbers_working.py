# Given an array of size N containing integers < M, with N >> M (e.g. there are duplicates), find the duplicates.

def find_duplicate_numbers(array):
    unique_values = list(set(array)) # create reference array of all unique values by converting list to set and back
    duplicates = list(set([i for i in array if not i in unique_values or unique_values.remove(i)]))
    return duplicates

if __name__ == '__main__':
    from sys import argv
    script, array = argv
    print find_duplicate_numbers(array)

# ==PSEUDOCODE==
# maybe there's a way to sort of "subtract" the lists from each other?
# transform list into set to get unique values?

# [i 
# for (i in a) 
# if (not i in b) 
# or ( b.remove(i) )]

# a = [1,2,3,3,3,3,4]
# b = [1,2,3,4]
# result: [2, 3, 3, 3, 4]