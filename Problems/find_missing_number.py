# find_missing_number - Given an array of size N with integers 1 to N+1, but missing one, find the missing number.

from sys import argv
import random
from random import shuffle

def generate_random_array():
    N = random.randint(1, 10000)
    array = [i for i in range(1, N + 1)]
    missing_number = random.randint(1, N)
    array.remove(missing_number)
    shuffle(array)
    print array
    return array, missing_number 

def find_missing_number(array):
    """Given an array of size N with integers 1 to N+1, but missing one, finds the missing number."""
    N = len(array) + 1
    return N * (N + 1) / 2 - sum(array)

if __name__ == "__main__":
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
    # random.seed(10) # can use to set seed
    N = random.randint(1, 40) # randomly generate N
    array = [i for i in range(1, N + 1)] # define array of values from 1 to N
    # random.seed(10)
    missing_number = random.randint(1, N) # randomly select number to delete from array
    print "missing_number:", missing_number
    array.remove(missing_number) # delete number from array
    shuffle(array)
    print array
    return array, missing_number # return finished array

def comments_find_missing_number(array):
    N = len(array) + 1 # rederive N, for accuracy
    return (N) * (N + 1) / 2 - sum(array) # find theoretical sum of array elements minus actual sum of array elements
    # less efficent: iterate through entries
    # for i in range(1, N + 1): # go through array from 1-N and search array for that value
    #     try:
    #         array.index(i) # look for that value in the array
    #     except ValueError: # if not found:
    #         return i # return the missing number



# Extra work on this problem from Keir
#
#   1. DONE Make the function take a single array argument (passing N is
#      unnecessary, you can derive N from the length of the array)
#   2. DONE Give the function a docstring.
#   3. DONE Write unit tests for the function.
#      a. DONE Write tests with explicit inputs (e.g. [1, 2, 4])
#      b. DONE Write tests with generated input (like your generate random array)
#   4. Extend the script using argparse (longer, means learning argparse)
#      a. To take a random seed
#      a. To take N
#      b. To take an array on the command line
#
# Number 4 is optional, but please do 1, 2, and 3.
