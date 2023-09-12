"""Little Sister's Vocabulary

https://exercism.org/tracks/python/exercises/little-sisters-vocab
"""

def add_prefix_un(word: str) -> str:
    """Prepend "un" to a string.

    :param word: - String of a root word.
    :return: - String of root word with un prefix.

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """
    return f"un{word}"


def make_word_groups(vocab_words: list[str]) -> str:
    """Apply the prefix in `vocab_words` to the rest of the words in `vocab_words`.

    :param vocab_words: - A list of vocabulary words with a prefix.
    :return: - String of prefix followed by vocabulary words with
               prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
    by ' :: '.
    """
    pfx = vocab_words[0]
    return " :: ".join(f"{pfx}{word}" if word != pfx else pfx for word in vocab_words)
    

def remove_suffix_ness(word: str) -> str:
    """Remove the suffic "ness" from a word.

    :param word: - String of word to remove suffix from.
    :return: - String of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """
    return f"{word[:-5]}y" if word[-5] == "i" else word[:-4]


def adjective_to_verb(sentence: str, index: int) -> str:
    """Add "en" to a target word in a sentence.

    :param sentence: - A sentence.
    :param index: - Index of the word to remove and transform.
    :return: - Word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the vocabulary word, and the 
    `index` of the word once that sentence is split apart.  The 
    function should return the extracted adjective as a verb.
    """    
    return f"{sentence[:-1].split()[index]}en"
    
