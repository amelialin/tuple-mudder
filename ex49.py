class ParserError(Exception): # creates a new exception class called ParserError that we can use
    pass

class Sentence(object): # create class called Sentence

    def __init__(self, subject, verb, obj):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1] # assigns the 2nd part of a tuple to the subject variable
        self.verb = verb[1]
        self.object = obj[1]

    def peek(word_list): # look at a list of words and return what kind of word it is
        if word_list: # if list is non empty
            word = word_list[0]
            return word[0] # e.g. 'noun', 'verb'
        else:
            return None

    def match(word_list, expecting): # confirms that the expected word is the right type, takes it off the list, and returns the word.
        if word_list: # if list is non empty
            word = word_list.pop(0) # pop first word into the word variable

            if word[0] == expecting: # if the word is of a type that matches what you were expecting
                return word
            else:
                return None
        else:
            return None

    def skip(word_list, word_type):
        while peek(word_list) == word_type:
            match(word_list, word_type)

    def parse_verb(word_list):
        skip(word_list, 'stop') # skip all the words like 'a', 'the', etc.

        if peek(word_list) == 'verb':
            return match(word_list, 'verb') # should return the word, if it's a verb
        else:
            raise ParserError("Expected a verb next.")

    def parse_object(word_list):
        skip(word_list, 'stop')
        next_word = peek(word_list)

        if next_word == 'noun':
            return match(word_list, 'noun')
        elif next_word == 'direction':
            return match(word_list, 'direction')
        else:
            raise ParserError("Expected a noun or direction next.")

    def parse_subject(word_list):
        skip(word_list, 'stop')
        next_word = peek(word_list)

        if next_word == 'noun':
            return match(word_list, 'noun')
        elif next_word == 'verb':
            return ('noun', 'player')
        else:
            raise ParserError("Expected a verb next.")

    def parse_sentence(word_list):
        subj = parse_subject(word_list)
        verb = parse_verb(word_list)
        obj = parse_object(word_list)

        return Sentence(subj, verb, obj)
