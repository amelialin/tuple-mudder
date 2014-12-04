# find_missing_number - Given an array of size N with integers 1 to N+1, but missing one, find the missing number.

def generate_random_array():
    # random.seed(10) # should I let the seed number be an input? How do I write unit tests for this problem?
    N = random.randint(1, 40)
    array = [i for i in range(1, N + 1)]
    # random.seed(10)
    missing_number = random.randint(1, N)
    array.remove(missing_number)
    shuffle(array)
    print array
    return array, N 

def find_missing_number():
    array, N = generate_random_array()
    return (N) * (N + 1) / 2 - sum(array)

if __name__ == "__main__":
    from sys import argv
    import random
    from random import shuffle
    print find_missing_number()

# ==PSEUDOCODE==
# As far as I can tell, there's no way to speed this one up. Just go through and mark off the numbers you find, and the remaining one is the one that's missing.
# solve for N, given size of input array
# go through from 1-N and search array for that value
    # if found
        # increment to next number
    # if not found
        # return that number

def comments_generate_random_array():
    # random.seed(10)
    N = random.randint(1, 40) # randomly generate N
    # print N
    array = [i for i in range(1, N + 1)] # define array of values from 1 to N
    # random.seed(10)
    missing_number = random.randint(1, N) # randomly select number to delete from array
    print "missing_number:", missing_number
    array.remove(missing_number) # delete number from array
    shuffle(array)
    print array
    return array, N # return finished array

def comments_find_missing_number():
    array, N = comments_generate_random_array() # get random array and N
    # print array
    # print N
    # for i in range(1, N + 1): # go through array from 1-N and search array for that value
    #     try:
    #         array.index(i) # look for that value in the array
    #     except ValueError: # if not found:
    #         return i # return the missing number
    return (N) * (N + 1) / 2 - sum(array) # find theoretical sum of array elements minus actual sum of array elements