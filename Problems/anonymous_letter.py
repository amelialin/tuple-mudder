# Write a function that takes two documents: an anonymous letter L and the text from a magazine M. Your function should return true if L can be written with words from M. Words from M can only be used in L as many times as they occur in M, just as though you were physically cutting up a magazine and pasting the words together.

from frequent_words import make_all_lowercase, strip_punctuation

def anonymous_letter(L, M):
    """Takes 2 strings as input, L and M. Returns True if L can be made from words in M, False if it cannot. Case insensitive and punctuation insensitive."""
    L_words = find_word_frequencies(make_all_lowercase(strip_punctuation(L)))
    M_words = find_word_frequencies(make_all_lowercase(strip_punctuation(M)))
    if set(L_words.keys()).issubset(set(M_words.keys())): # test if all words in L are in M
        pass
    else:
        return False
    for word in L_words.keys(): # test if all frequencies of words in L are <= frequencies of words in M
        print word, L_words[word], M_words[word]
        if L_words[word] <= M_words[word]:
            pass
        else:
            return False
    return True

def find_word_frequencies(string): # modified frequent_words
    """Takes input as a string, returns dict of all words, made lowercase, and their frequencies. Case insensitive. Input will be stripped 
    of common punctuation."""
    word_frequencies = {}
    string = make_all_lowercase(strip_punctuation(string)) 
        # clean up string
    words = string.split()
    for word in words:
        if word_frequencies.get(word) == None: 
            word_frequencies[word] = 1 
        else:
            word_frequencies[word] += 1
    return word_frequencies

if __name__ == "__main__":
    from sys import argv
    script, L, M = argv
    print anonymous_letter(L, M)

# ==PSEUDOCODE==

# You could do something really hacky where you go through all the combinatorial possibilities for every subset of M and see if L equals any of them

# Better would be to at least get the total set of all words from L and set of all words from M, and make sure that L is in M. Then, check the *counts* for each of those words and make sure that the count for each word in L is <= the count of the same word in M. Seems like a dict would be good here, similar to frequent_words. Honestly using frequent_words and just plugging L and M into it, then comparing, seems like a perfectly reasonable way to go about this.