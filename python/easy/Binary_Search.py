"""Binary Search

https://exercism.org/tracks/python/exercises/binary-search
"""

def find(numbers: list[int], number: int) -> int:
    """Return the index of a number in a list of numbers via binary search.
    
    :param numbers: - A list of integers.
    :param number: - An integer number to find the index of within `numbers.
    :raise ValueError: - If the given `number` is not in the given list of `numbers`
                         or an empty list is passed for `numbers`.
    :return: - The index of a `number` within a list of `numbers`.
    """
    start = 0
    end = len(numbers) - 1

    if numbers:
        while start <= end:
            half = (start + end) // 2
            target = numbers[half]
            if target > number:
                end = half - 1
            elif target < number:
                start = half + 1
            else:
                return half

    raise ValueError("value not in array")
