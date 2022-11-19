"""Sum of Multiples

https://exercism.org/tracks/python/exercises/sum-of-multiples
"""

def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """Return the sum of all the unique given multiples.
    
    :param limit: - Range UP TO the given limit to check for multiples.
    :param multiples: - Only numbers which evenly divide by values in `multiples` will be summed.
    :return: - The sum of all unique multiples from `multiples` of numbers in the `limit` range.
    """
    return sum({n for n in range(limit) 
                  for f in multiples 
                  if f 
                  and n%f == 0})
