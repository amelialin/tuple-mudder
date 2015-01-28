from frequent_words import frequent_words

def test_frequent_words():

# how to write accurate tests here?

    assert frequent_words("The the the the quick quick quick brown brown fox").issubset(set(['the', 'quick', 'brown']))
    assert frequent_words("The the quick quick the quick brown brown the fox").issubset(set(['the', 'quick', 'brown']))
    assert frequent_words("The") == "Input must have at least 3 different words."
    assert frequent_words("Wordcounter ranks the most frequently used words in any given body of text. Use this to see what words you overuse (is everything a 'solution' for you?) or maybe just to find some keywords from a document. Wordcounter is useful for writers, editors, students, and anyone who thinks that they might be speaking redundantly or repetitively -- and it's free! Eventually, I'm going to expand it so that you can upload documents, but not yet.").issubset(set(['you', 'to', 'a', 'wordcounter', 'that', 'or', 'for', 'and', 'is', 'words', 'it']))