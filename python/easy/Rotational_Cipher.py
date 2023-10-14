"""Rotational Cipher

https://exercism.org/tracks/python/exercises/rotational-cipher
"""

def rotate(text: str, key: int) -> str:
    """Perform a rotational cipher operation on the given text with the given key as rotations.
    
    :param text: - String to convert to cypher text via character rotation.
    :return rotation: - Cypher text of given `text` via character rotation.
    """
    rotation = ""
    for c in text:
        # rotational logic
        cycle = lambda char, key, scope: chr((ord(char) + key - scope) % 26 + scope)
        
        rotation += (cycle(c, key, 65) if c.isupper() else # rotate upper case letters
                     cycle(c, key, 97) if c.islower() else # rotate lower case letters
                     c)                                    # do NOT rotate non-letters
            
    return rotation

# # credit to xelf#7577 in the python Discord: https://discord.com/invite/python
# from string import ascii_lowercase as abc, ascii_uppercase as ABC
# def rotate(text, k):
#     k = k%26
#     d = dict(zip(abc, abc[k:]+abc[:k]))
#     d |= dict(zip(ABC, ABC[k:]+ABC[:k]))
#     return text.translate(''.maketrans(d))
