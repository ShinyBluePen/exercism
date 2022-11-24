"""Nth Prime

https://exercism.org/tracks/python/exercises/nth-prime

Very efficient solution"
https://stackoverflow.com/questions/53481804/time-limit-exceeded-python/53483084#53483084
"""

def prime(n: int) -> int:
    """Return the n'th prime number."""
    if n < 1: raise ValueError('there is no zeroth prime')

    prime_list = [2]        # initial prime number list
    cand = 3                 # first number to test if prime
    
    while len(prime_list) < n: # keep generating primes until we get to the nth one
        for p in prime_list:    # check if cand is divisible by any prime before it
            if cand % p == 0:    # if there is no remainder then the candidate is not prime
                break             # break to stop testing more candidates
                                   # if the candidate is prime, add it to the list
        else:                       # after a for loop, else runs if there was no `break`
            prime_list.append(cand)  # append to prime list
            
        cand += 2                      # don't check even numbers
        
    return prime_list[-1]                # return the last prime number generated
    
