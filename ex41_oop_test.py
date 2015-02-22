import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# dict of flashcards, where keys are code and values are English translations
PHRASES = {
    "class %%%(%%%):": "Make a class named %%% that is-a %%%.", 
    "class %%%(object): \n\tdef __init__(self, ***)" : "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object): \n\tdef ***(self, @@@)": "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)": "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip()) # strips whitespace chars from beginning and end of strings
    # now you have a list WORDS composed of lots of words!

def convert(snippet, phrase): # snippet is the code, phrase is the english translation
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))] # Count how many %%%s are in a snippet. Take that many random words, without replacement, from WORDS. Capitalize them. Stick them in class_names.
    other_names = random.sample(WORDS, snippet.count("***")) # Do the same thing now but with ***s
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count))) # Takes a random sample of 1-3 words from WORDS. Joins all the words together, separated by commas. Appends all of this to param_names. The random sampling of 1-3 is to create functions that take anywhere from 1-3 parameters.

    for sentence in snippet, phrase: # do the following stuff first for the snippet, then second for the phrase (2x total)
        result = sentence[:] # makes copy of a list

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1) # takes each single instance of %%% and replaces it with a different fake class name. This relies on the fact that each class name is only used once per snippet and phrase, e.g. there is no phrase that looks like "There is a class named X, and in X there is a function..."

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results # this is a list with 2 items, the first is the snippet with all fake values filled in, and the second is the phrase with all fake values filled in.

# keep going until they hit CTRL-D
try:
    while True: # loop forever
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase) # fill in with fake values
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER:  %s\n\n" % answer # merely spits out the "answer", doesn't check for the user if it's right

except EOFError: # if they hit Ctrl-D
    print "\nBye"