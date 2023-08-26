"""Square Root

https://exercism.org/tracks/python/exercises/square-root
"""

def square_root(number: int) -> int:
    """Return the root of a perfect square, or the closest square rounded up.
    
    :param number: - A given perfect square.
    :return root: - The square root of `number`.
    """
    return number ** 0.5
    # # determine root by repeated subtraction of odd numbers
    # n = number
    # root = 0
    # for i in range(number+1):
    #     if i % 2:
    #         n -= i
    #         root += 1
    #     if n <= 0:
    #         return root

# # pythons math.sqrt() function:
    # https://github.com/python/cpython/blob/main/Modules/mathmodule.c#:~:text=Here%27s%20Python%20code%20equivalent%20to%20the%20C%20implementation%20below%3A
    # import operator
    # n = operator.index(number)
    # if n < 0:
    #     raise ValueError("isqrt() argument must be nonnegative")
    # if n == 0:
    #     return 0
    # c = (n.bit_length() - 1) // 2
    # a = 1
    # d = 0
    # for s in reversed(range(c.bit_length())):
    #     # Loop invariant: (a-1)**2 < (n >> 2*(c - d)) < (a+1)**2
    #     e = d
    #     d = c >> s
    #     a = (a << d - e - 1) + (n >> 2*c - e - d + 1) // a
    # return a - (a*a > n)
