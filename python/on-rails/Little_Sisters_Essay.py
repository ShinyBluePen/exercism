"""Little Sister's Essay

https://exercism.org/tracks/python/exercises/little-sisters-essay
"""

def capitalize_title(title: str) -> str:
    """Capitalize the first letter of a string.

    :param title: - Title string that needs title casing.
    :return: - Title string in title case (first letters capitalized).
    """
    return title.title()


def check_sentence_ending(sentence: str) -> bool:
    """Check if a string ends in a period character.

    :param sentence: - A sentence to check.
    :return: - True if punctuated correctly with period, False otherwise.
    """
    return sentence.endswith(".")


def clean_up_spacing(sentence: str) -> str:
    """Remove leading and trailing whitespaces from a string.

    :param sentence: - A sentence to clean of leading and trailing space characters.
    :return: - A sentence that has been cleaned of leading and trailing space characters.
    """
    return sentence.strip()


def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
    """Replace all occurances of `old_word` with `new_word` in `sentence`.

    :param sentence: - A sentence to replace words in.
    :param old_word: - Word to replace.
    :param new_word: - Replacement word.
    :return: - Input sentence with new words in place of old words.
    """
    return sentence.replace(f" {old_word}", f" {new_word}")
