"""Handshake

https://exercism.org/tracks/python/exercises/secret-handshake
"""

def commands(binary_str: str) -> list[str]:
    """Given a binary string of 5 digits, return a list of instructions.
    
    :param binary_str: - A string of 5 binary digits.
    :return handshake: - Sequence of instructions deduced from `binary_str`.
    """
    handshake = []
    if binary_str[4] == '1': handshake.append("wink")
    if binary_str[3] == '1': handshake.append("double blink")
    if binary_str[2] == '1': handshake.append("close your eyes")
    if binary_str[1] == '1': handshake.append("jump")
    if binary_str[0] == '1': handshake.reverse()
        
    return(handshake)
