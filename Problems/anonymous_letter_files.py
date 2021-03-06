# Write a function that takes two documents: an anonymous letter L and the text 
# from a magazine M. Your function should return true if L can be written with 
# words from M. Words from M can only be used in L as many times as they occur 
# in M, just as though you were physically cutting up a magazine and pasting 
# the words together.

from frequent_words import make_all_lowercase, strip_punctuation

def anonymous_letter_files(L_file, M_file):
    """Takes 2 filenames as input, which contain text. Returns True if the text 
    in L can be made from words in M, False if it cannot. Case insensitive and 
    punctuation insensitive."""
    L_words = find_word_frequencies(
        make_all_lowercase(strip_punctuation(open(L_file).read())))
    M_words = find_word_frequencies(
        make_all_lowercase(strip_punctuation(open(M_file).read())))
    
    # test if all words in L are in M
    if set(L_words.keys()).issubset(set(M_words.keys())): 
        pass
    else:
        return False
    
    # test if all frequencies of words in L are <= frequencies of words in M
    for word in L_words.keys(): 
        print word, L_words[word], M_words[word]
        if L_words[word] <= M_words[word]:
            pass
        else:
            return False
    return True

def find_word_frequencies(string): # modified frequent_words
    """Takes input as a string, returns dict of all words, made lowercase, 
    and their frequencies. Case insensitive. Input will be stripped 
    of common punctuation."""
    word_frequencies = {}
    string = make_all_lowercase(strip_punctuation(string)) # clean up string
    words = string.split()
    for word in words:
        if word_frequencies.get(word) == None: 
            word_frequencies[word] = 1 
        else:
            word_frequencies[word] += 1
    return word_frequencies

if __name__ == "__main__":
    from sys import argv
    script, L_file, M_file = argv
    print anonymous_letter_files(L_file, M_file)