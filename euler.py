import math


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
