# Find the three most frequently occurring words in an article.
# Computational complexity of O(n), couldn't see anything here that would do
# anything other than scale linearly with the length of the string.

class InputError(Exception):
    pass

def frequent_words(string):
    """Takes input as a string, returns set of top 3 most frequent words, 
    all lowercase. Words of equal frequency treated equally when deciding which
    to include in the top 3. Case insensitive. Input will be stripped 
    of common punctuation. Input must have at least 3 different words."""
    word_frequencies = {}
    words = strip_punctuation(string).lower().split()
    for word in words:
        if word_frequencies.get(word) == None: 
            word_frequencies[word] = 1 
        else:
            word_frequencies[word] += 1
    if len(word_frequencies) < 3: # check for inappropriate input
        raise InputError("Input must have at least 3 different words.")
    items = word_frequencies.items()
    items.sort(key=lambda key_value: key_value[1], reverse=True)
    return set(key_value[0] for key_value in items[:3])

    # "lambda key_value: key_value[1]" lambda function with single variable key_value, and then what you want to do with that key_value
    # reverse = go from largest to smallest instead of smallest to largest
    # sort expects to see a function that takes one parameter, lambda is commonly used
    # no need to give "key" a value if you wanting to sort the default thing, the first part of the tuple
    # for slicing, think of the : as "the farthest thing towards that end", in the format (x:y) where x is the beginning of the slice and y is the end of the slice

def strip_punctuation(string):
    """Removes common punctuation from a string."""
    return "".join(ch for ch in string if ch not in ',.!?:;-/)(')

def make_all_lowercase(string):
    """Takes a string and outputs same string all in lowercase."""
    return string.lower()

if __name__ == "__main__":
    from sys import argv
    print frequent_words(argv[1])
