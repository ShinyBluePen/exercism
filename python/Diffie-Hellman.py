"""Diffie-Hellman

https://exercism.org/tracks/python/exercises/diffie-hellman
"""

import secrets

def private_key(p: int) -> int:
    """Generate a private key greater than 1 and less than `p`.
    
    :param p: - A random prime integer.
    :return: - A random integer chosen from between 2 and `p` (inclusive).
    """
    return secrets.choice(range(2, p))

def public_key(p: int, g: int, private: int) -> int:
    """Generate a public key.
    
    :param p: - A random prime integer previously determined by `private_key`.
    :param g: - A random prime number.
    :param private: - Output of `private_key`.
    :return: - g**private % p.
    """
    return pow(g, private, p)

def secret(p: int, public: int, private: int) -> int:
    """Generate a shared secret key.
    
    :param p: - A random prime integer previously determined by `private_key`.
    :param public: - Output of `public_key`.
    :param private: - Output of `private_key`.
    :return: - public**private % p.
    """
    return pow(public, private, p)
