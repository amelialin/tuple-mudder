# Given an array of size N containing integers < M, with N >> M (e.g. there are duplicates), find the duplicates.

def find_duplicate_numbers(array):
    """Given a list, returns set of duplicate entries."""
    unique_values = list(set(array)) # create reference array of all unique values by converting list to set and back
    duplicates = set([i for i in array if not i in unique_values or unique_values.remove(i)])
    return duplicates

if __name__ == '__main__':
    from sys import argv
    # script, array = argv # you actually don't have to do this, argv is an array already, this just assigns the values from the arrays to variables
    print find_duplicate_numbers(argv[1:]) # this says take everything from argv[1] to the last element and use that subarray as input. We don't want argv[0] since that's just the script.

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