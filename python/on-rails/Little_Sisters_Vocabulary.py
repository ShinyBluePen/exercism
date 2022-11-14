"""Little Sister's Vocabulary

https://exercism.org/tracks/python/exercises/little-sisters-vocab
"""

def add_prefix_un(word: str) -> str:
    """
 
    :param word: str - Stringof a root word.
    :return: str - String of root word with un prefix.
 
    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """
    
    return f"un{word}"
  
def make_word_groups(vocab_words: list[str, ...]) -> str:
    """
 
    :param vocab_words: list[str, ...] - List of vocabulary words with a prefix.
    :return: str - String of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.
 
    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    pfx = vocab_words[0]
    prefixed_list = [pfx]
    
    for word in vocab_words[1::]:
        word = pfx + word
        prefixed_list.append(word)
    
    return " :: ".join(prefixed_list)
  
def remove_suffix_ness(word: str) -> str:
    """
 
    :param word: str - String of word to remove suffix from.
    :return: str - String of word with suffix removed & spelling adjusted.
 
    This function takes in a word and returns the base word with `ness` removed.
    """
    sfx = "ness"
    if sfx in word:
        if word[-5] == "i":
            word = word[:-5] + "y"
        else:
            word = word[:-4]
        
        return word
      
def adjective_to_verb(sentence: str, index: int) -> str:
    """
 
    :param sentence: str - string that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - string word that changes the extracted adjective to a verb.
 
    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    if "." in sentence:
        sentence = sentence[:-1]
        sentence = sentence.split()
    else:
        sentence = sentence.split()
    
    adj = sentence[index]
    verbed_abj = adj + "en"
    
    return verbed_abj
  
