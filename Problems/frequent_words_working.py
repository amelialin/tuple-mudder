# Find the three most frequently occurring words in an article.

def frequent_words(original_string):
    """Takes input as a string, returns list of top 3 most frequent words, all lowercase, in order of decreasing frequency. Words of equal frequency are equally likely to be listed. Case insensitive. Input will be stripped of common punctuation. Input must have at least 3 different words."""

    string = make_all_lowercase(strip_punctuation(original_string))
    word_frequencies = {} # initialize an empty dict
    words = string.split() # put words into a list
    # print "words:", words
    for word in words: # parse the article word by word
        if word_frequencies.get(word) == None: # if you come across a new word that doesn't already exist in the dict
            # print word, "not found"
            word_frequencies[word] = 1 # add a new key in the dict, and set the value to 1
        else: # if the word already exists
            # print word, "found"
            word_frequencies[word] += 1 # increment the value by 1
    # print "word_frequencies:", word_frequencies
    # after you're done, look through the whole dict for the 3 keys with the highest values.
    kv = word_frequencies.items()
    # print "kv:", kv
    if len(kv) < 3:
        return "Input must have at least 3 different words."
    k = word_frequencies.keys() # dump all keys into a list
    v = word_frequencies.values() # dump all values into a list
    print "k:", k
    print "v:", v

    v_top = [0, 0, 0]
    k_top = [None, None, None]

    for i in range(3):
        top_index = v.index(max(v)) # find index of highest value
        top_value = v[top_index] # find the highest value
        top_key = k[top_index] # find the highest key
        print "top_value:", top_value
        print "top_key:", top_key
        v_top[i] = top_value # stick those into lists
        k_top[i] = top_key
        del v[top_index] # remove those entries
        del k[top_index]
        # print "k:", k
        # print "v:", v

    print "v_top:", v_top
    print "k_top:", k_top

    return k_top

def make_all_lowercase(string):
    """Takes a string and outputs same string all in lowercase."""
    return string.lower()

def strip_punctuation(string):
    """Removes common punctuation from a string."""
    stripped_string = "".join(ch for ch in string if ch not in (',', '.', '!', '?', ':', ';', '-', '/', ')', '('))
    return stripped_string

if __name__ == "__main__":
    from sys import argv
    script, string = argv
    print frequent_words(string)

# ==PSEUDOCODE==
# initialize an empty dict
# parse the article word by word
    # if you come across a new word that doesn't already exist in the dict
        # add a new key in the dict, and set the value to 1
    # if the word already exists
        # increment the value by 1
# after you're done, look through the whole dict for the 3 keys with the highest values.