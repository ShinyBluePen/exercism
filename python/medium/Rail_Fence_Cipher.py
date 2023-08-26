"""Rail Fence Cipher

https://exercism.org/tracks/python/exercises/rail-fence-cipher
"""

def zig_positions(msg_length: int, rails: int) -> tuple[int, int]:
    """Generate appropriate posistions for encoding and decoding an RFC array.
    
    :param msg_length: - The length of the message.  Needed to determine row length.
    :param rails: - Number of "rails"; rows.
    :return coord: - The returned coords represent the zig-zag pattern of RFC.
    """
    x = 0
    y = 0
    for position in range(msg_length):
        coord = (x, y) # the first position is always in the top left corner
        y += 1 # we always place each letter to the right of the last
        
        # x positioning logic
        if x == 0: 
            reverse = False
        if x == rails-1: 
            reverse = True
            
        if not reverse: 
            x += 1
        if reverse: 
            x -= 1

        yield coord

def fill(message: str, rails: int, decode: bool=False) -> list[str, str]:
    """Fill an array from left to right, rail by rail in a zig-zag pattern.

    :param message: - String to fill into the `zigged_array`.
    :param rails: - Number of "rails"; rows.
    :return zigged_array: - a zigged array filled with `message` in the RFC pattern.
    """
    zigged_array = [[None] * len(message) for i in range(rails)]
        
    for x, y in zig_positions(len(message), rails):
        zigged_array[x][y] = message[y]
    
    msg_index = 0
    if decode:
        for i, line in enumerate(zigged_array):
            for j, letter in enumerate(line):
                if letter:
                    zigged_array[i][j] = message[msg_index]
                    msg_index += 1

    return zigged_array

def encode(message: str, rails: int) -> str:
    """Encode a message via RFC.

    :param message: - String to be ciphered.
    :param rails: - Number of rails for the cipher.
    :return: - RFC ciphertext of `message`.
    """
    message = message.replace(" ", "")
    return "".join([ltr for line in fill(message, rails) for ltr in line if ltr])

def decode(encoded_message: str, rails: int) -> str:
    """Decode an RFC encoded message.
    
    :param encoded_message: - Cipher text to decode.
    :param rails: - Number of rails for the cipher.
    :return: - Decoded RFC cipher text from `encoded_message`.
    """
    msg = encoded_message
    encoded_array = fill(msg, rails, decode=True)

    return "".join(encoded_array[x][y] for x, y in zig_positions(len(msg), rails))
