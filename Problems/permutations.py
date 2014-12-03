# Print all permutations of a string.

def permutations(string):
    length_of_string = len(string)
    all_permutations = []
    current_permutation_list = ""
    remainder_string = string
    remainder_list = list(remainder_string)
    permutations_helper(current_permutation_list, remainder_string, all_permutations)
    return all_permutations

def permutations_helper(current_permutation_list, remainder_string, all_permutations):
    remainder_list = list(remainder_string) 
    length_of_remainder = len(remainder_list)
    if len(remainder_list) == 1:
        current_permutation_list += remainder_list[0]
        all_permutations.append(current_permutation_list)
    else:
        for i in range(length_of_remainder):
            current_permutation_sublist = current_permutation_list[:]
            current_permutation_sublist += remainder_list[i]
            remainder_sublist = remainder_list[:]
            del remainder_sublist[i]
            remainder_string = ''.join(remainder_sublist)
            permutations_helper(current_permutation_sublist, remainder_string, all_permutations)

if __name__ == "__main__":
    from sys import argv
    script, string = argv
    print permutations(string)

# ==PSEUDOCODE==

# ==Recursive Soln==
# If the REMAINDER set has > 1 character left
    # take the next character and append it to the end of the PERMUTATION string
    # mark that this branch has been taken
# Otherwise, if the REMAINDER set has only one character, append it to the end of the PERMUTATION string

# ==Iterative Soln==
# a lot of nested for loops; as many as there are characters in the string
# for (0, number_of_characters)
# append each result to an array, total array will contain all permutations. There will always be number_of_chracters! (factorial) number of results

def comments_permutations(string):
    length_of_string = len(string)
    all_permutations = [] # initialize empty result list
    current_permutation_list = "" # initialize empty string for current permutation head
    remainder_string = string # for first iteration, the remainder is the entire string
    remainder_list = list(remainder_string) # transform string into list form
    print "current_permutation_list:", current_permutation_list, "remainder_list:", remainder_list
    comments_permutations_helper(current_permutation_list, remainder_string, all_permutations) # run permutations_helper, which will build all_permutations for us
    return all_permutations # simply return the updated all_permutations list

def comments_permutations_helper(current_permutation_list, remainder_string, all_permutations): # this helper function takes more inputs to pass information between levels of recursion. all_permutations is simply a *reference* to the list, which is accessible at all levels of the recursion.
    remainder_list = list(remainder_string) # listify the string you passed in
    length_of_remainder = len(remainder_list)
    if len(remainder_list) == 1: # if there's only one character left (only 1 possibility what's coming next):
        print "current_permutation_list:", current_permutation_list, "remainder_list:", remainder_list
        current_permutation_list += remainder_list[0] # append the lone character to the end of the current_permutation_list to complete the permutation
        all_permutations.append(current_permutation_list) # append the completed permutation to the master list all_permutations
        print "all_permutations:", all_permutations
    else: # if there is >1 character left:
        for i in range(length_of_remainder): # for each possible *next* character (since there is >1 possibility what the next char is):
            current_permutation_sublist = current_permutation_list[:] # make a copy of the current "head" of the word. A *separate* copy of current_permutation_sublist will live in *each* level of recursion!
            current_permutation_sublist += remainder_list[i] # append the character to the head
            remainder_sublist = remainder_list[:] # make a copy of the current "remainder" of the word
            del remainder_sublist[i] # delete the character from the remainder, since it has now been "used up"
            print "current_permutation_sublist:", current_permutation_sublist, "remainder_sublist:", remainder_sublist            
            remainder_string = ''.join(remainder_sublist) # stringify the remaining remainder, to be used as input in next level of recursion
            comments_permutations_helper(current_permutation_sublist, remainder_string, all_permutations) # find all permutations of the new, shorter remainder