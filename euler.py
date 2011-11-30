import math


def ispalindrome(x):
    """
    Check if x is a palindrome.
    """

    return str(x) == str(x)[::-1]


def ispandigital(x):
    """
    Check if x is pandigital.

    An n-digit number is pandigital if it makes use of all the digits 1
    to n exactly once.
    """

    digits = len(str(x))
    return sorted([int(c) for c in str(x)]) == range(1, digits + 1)


def isprime(x):
    """
    Check if x is prime.
    """

    if x < 2:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True
