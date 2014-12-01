# Print all permutations of a string.

def permutations(string):
    length_of_string = len(string)
    all_permutations = []
    current_permutation_list = "" # initialize empty string
    remainder_string = string # for first iteration, the 
        # remainder is the entire string
    remainder_list = list(remainder_string) # transform 
        # into list form
    print "Input string: %s Length of string: %d" % (string, length_of_string)
    permutations_helper(current_permutation_list, remainder_string, all_permutations)
    return all_permutations

def permutations_helper(current_permutation_list, remainder_string, all_permutations): # takes more 
        # inputs to pass values of variables between
        # levels of recursion
    remainder_list = list(remainder_string) 
    length_of_remainder = len(remainder_list)
    print "current_permutation_list:", current_permutation_list, "remainder_list:", remainder_list, "with", len(remainder_list), "elements left. all_permutations:", all_permutations
    if len(remainder_list) == 1:
        print "Only 1 element left"
        print "current_permutation_list:", current_permutation_list
        current_permutation_list += remainder_list[0]
        print "current_permutation_list:", current_permutation_list
        all_permutations.append(current_permutation_list)
        print "all_permutations:", all_permutations
        print "FINAL All Permutations:", all_permutations
        # return all_permutations
    else:
        print "%d elements left" % length_of_remainder
        print range(length_of_remainder)
        for i in range(length_of_remainder):
            print "i:", i
            current_permutation_sublist = current_permutation_list[:]
            current_permutation_sublist += remainder_list[i]
            remainder_sublist = remainder_list[:]
            del remainder_sublist[i]
            remainder_string = ''.join(remainder_sublist)
            print "Running recursion. current_permutation_sublist:", current_permutation_sublist, "remainder_sublist:", remainder_sublist, "all_permutations:", all_permutations
            permutations_helper(current_permutation_sublist, remainder_string, all_permutations)

if __name__ == "__main__":
    from sys import argv
    script, string = argv
    print permutations(string)

# ==PSEUDOCODE==

# ==Recursive Soln==
# create tracker list that records what branch of the total possibility tree you are at
# If the REMAINDER set has > 1 character left
    # take the next character and append it to the end of the PERMUTATION string
    # mark that this branch has been taken
# Otherwise, if the REMAINDER set has only one character, append it to the end of the PERMUTATION string

# ==Iterative Soln==
# a lot of nested for loops; as many as there are characters in the string
# for (0, number_of_characters)
# append each result to an array, total array will contain all permutations. There will always be number_of_chracters! (factorial) number of results

# 123
# 132
# 213
# 231
# 312
# 321
