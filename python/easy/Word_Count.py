"""Word Count

https://exercism.org/tracks/python/exercises/word-count
"""

def count_words(sentence: str) -> dict[str: int]:
    """Count whitespace seperated words and numbers in a string.
    
    :param sentence: - A string of words and/or digit numbers to count.
    :return word_count: - A dictionary with in the form of {"word": count}.
    """    
    # not filtering quotes -> (', ")
    punc_filter = "!@#$%^&*()[]{}_-+=:;,.<>/|\~`"

    # clean the string
    clean_sentence = "".join([c if c not in punc_filter else " " for c in sentence.lower()])

    # count words
    word_count = dict()
    word_list = clean_sentence.split()
    for word in word_list:
        if word == "'" or word == "\"":
            continue
        # strip any quotes
        word = word.strip("'\"") # won't strip if `word` is a quote
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
                
    return word_count
