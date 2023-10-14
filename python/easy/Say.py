"""Say

https://exercism.org/tracks/python/exercises/say

After many hours working on this, and coming close but 
regretibly not quite there, the following code is stolen from @Mattehbt.
https://exercism.org/tracks/python/exercises/say/solutions/Mattehbt

@ysf also did an excellent and amazing job.
https://exercism.org/tracks/python/exercises/say/solutions/ysf

So did @liweinan0423
https://exercism.org/tracks/python/exercises/say/solutions/liweinan0423
"""

DIGITS = { 
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
    }

TENS = (
    'zero',
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
    )

SCALES = (
    (100,           1_000,             "hundred" ),
    (1_000,         1_000_000,         "thousand"),
    (1_000_000,     1_000_000_000,     "million" ),
    (1_000_000_000, 1_000_000_000_000, "billion" ),
    )

def say(number: int) -> str:
    """Convert an integer `number` to it's "spoken" equivalent.

    :param number: - An integer between 0 and 999_999_999_999.
    :return: - The spoken equivalent of a given `number`.
    """
    if number < 0 or number > 999_999_999_999:
        raise ValueError('input out of range')
        
    if number < 20:                   # line 73 logic explanation:
        return DIGITS[number]         # create a tuple and use a bool index to choose an option
                                      # Example:    `("abc", "")[x == 1]`
    if number < 100:                  # equivalent: `"" if x == 1 else "abc"`
                # pull out 20-80
        return (f"{TENS[number // 10]}"
                # pull out 0-9                    # check if one's place is 0
                f"{(f'-{DIGITS[number % 10]}', '')[number % 10 == 0]}")
        
    for lower, upper, scale in SCALES:
        if number < upper:
            return (f"{say(number // lower)} {scale}"
                    f"{(f' {say(number % lower)}', '')[number % lower == 0]}")
