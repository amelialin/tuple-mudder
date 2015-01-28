# Find the three most frequently occurring words in an article.

def frequent_words(original_string):
    """Takes input as a string, returns set of top 3 most frequent words, 
    all lowercase. Words of equal frequency treated equally when deciding which
    to include in the top 3. Case insensitive. Input will be stripped 
    of common punctuation. Input must have at least 3 different words."""
    word_frequencies = {}
    string = make_all_lowercase(strip_punctuation(original_string)) 
        # clean up string
    words = string.split()
    for word in words:
        if word_frequencies.get(word) == None: 
            word_frequencies[word] = 1 
        else:
            word_frequencies[word] += 1
    kv = word_frequencies.items()
    if len(kv) < 3: # check for inappropriate input
        return "Input must have at least 3 different words."
    k = word_frequencies.keys()
    v = word_frequencies.values()
    k_top = set()
    for i in range(3):
        top_index = v.index(max(v))
        top_key = k[top_index]
        k_top.update([top_key]) # why do I need the '[]'?
        del v[top_index]
        del k[top_index]
    return k_top

def make_all_lowercase(string):
    """Takes a string and outputs same string all in lowercase."""
    return string.lower()

def strip_punctuation(string):
    """Removes common punctuation from a string."""
    stripped_string = "".join(ch for ch in string if ch not in (',', '.', '!', 
        '?', ':', ';', '-', '/', ')', '('))
    return stripped_string

if __name__ == "__main__":
    from sys import argv
    script, string = argv
    print frequent_words(string)