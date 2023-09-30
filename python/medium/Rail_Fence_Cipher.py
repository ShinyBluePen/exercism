"""Rail Fence Cipher

https://exercism.org/tracks/python/exercises/rail-fence-cipher
"""

def calculate_rail_indices(message: str, rails: int) -> list[int]:
    """Generate appropriate posistions for encoding and decoding an RFC array.
    
    :param message: - String to be ciphered.
    :param rails: - Number of "rails"; rows.
    :return: - Return a list of "rail" indices in a "fence" pattern.
    """
    cycle_length = (rails - 1) * 2  # Calculate the length of each cycle

    rail_indices = []
    for i, char in enumerate(message):
        cycle_position = i % cycle_length
        rail_index = min(cycle_position, cycle_length - cycle_position)
        rail_indices.append(rail_index)

    return rail_indices


def encode(message: str, rails: int) -> str:
    """Encode a message via RFC.

    :param message: - String to be ciphered.
    :param rails: - Number of rails for the cipher.
    :return: - RFC ciphertext of `message`.
    """
    rail_indices = calculate_rail_indices(message, rails)
    
    return "".join(c for c, i in sorted(zip(message, rail_indices), key=lambda x: x[1]))


def decode(ciphertext: str, rails: int) -> str:
    """Decode an RFC encoded message.
    
    :param ciphertext: - Cipher text to decode.
    :param rails: - Number of rails for the cipher.
    :return: - Decoded RFC cipher text from `ciphertext`.
    """
    rail_indices = calculate_rail_indices(ciphertext, rails)
    positions = sorted(range(len(ciphertext)), key=lambda x: rail_indices[x])
    
    return "".join(ciphertext[positions.index(i)] for i in range(len(ciphertext)))
