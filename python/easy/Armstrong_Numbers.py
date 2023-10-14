"""Armstrong Numbers

https://exercism.org/tracks/python/exercises/armstrong-numbers
"""

def is_armstrong_number(number: int) -> bool:
    """Test if a given number passes the Armstrong algorythm.
    
    :param number: int - Given number to check.
    :return: bool - True if the giveen `number` is an Armstrong number.
    
    An Armstrong number is a number that is the sum of its own digits 
    each raised to the power of the number of digits.
    """
    numbers = [int(digit) for digit in str(number)]
    return number == sum([digit**len(numbers) for digit in numbers])
