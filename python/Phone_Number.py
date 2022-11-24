"""Phone Number

https://exercism.org/tracks/python/exercises/phone-number
"""

import string

def parse_number(number: str) -> str:
    """Error check a NANP phone number and return a processed number.
    
    :param number: - A string of numbers to parse.
    :return num: - A string of numbers suitable for evaluation.
    """
    if set(string.ascii_letters).intersection(number):
        raise ValueError("letters not permitted")
    if set("@:!").intersection(number):
        raise ValueError("punctuations not permitted")

    # format the number by removing anything but the digits.
    num = "".join([d for d in number if d.isdigit()])
    
    if len(num) < 10:
        raise ValueError("incorrect number of digits")
    if len(num) > 11:
        raise ValueError("more than 11 digits")
    if len(num) == 11 and num[0] != "1":
        raise ValueError("11 digits must start with 1")

    # remove country code
    if num[0] == "1" and len(num) == 11:
        num = num[1:]
    
    if num[0] == "0": raise ValueError("area code cannot start with zero")
    if num[0] == "1": raise ValueError("area code cannot start with one")
    if num[3] == "0": raise ValueError("exchange code cannot start with zero")
    if num[3] == "1": raise ValueError("exchange code cannot start with one")
        
    return num

class PhoneNumber:
    """Creates and manages North American Numbering Plan (NANP) phone numbers.
    
    NANP numbers are ten-digit numbers consisting of a three-digit
    Numbering Plan Area code, commonly known as an area code, followed
    by a seven-digit local number. The first three digits of the local
    number represent the exchange code, followed by the unique four-digit
    number which is the subscriber number.
    
    N is any digit 2-9 and X is any digit 0-9.
          |-------> local number
    (NXX)-NXX-XXXX
    |     |   |---> subscriber number
    |     |-------> exchange code
    |-------------> NP area code

    Parameters:
    :number: str - A NANP number.
    
    Attributes:
    :number: str - A parsed version of the given `number` parameter.
    :area_code: str - number[:3].
    :local_number: str - number[3:10].
    :exchange_code: str - number[3:6].
    :subscriber_number: str - number[6:10].

    Methods:
    :pretty(self): - Return a formatted version of the given number.
    """
    def __init__(self, number: str) -> None:
        self.number = parse_number(number)
        self.area_code = self.number[:3]
        self.local_number = self.number[3:10]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[6:10]

    def pretty(self) -> str:
        """Print a formatted version of the phone number: (NXX)-NXX-XXXX."""
        return (f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}")
