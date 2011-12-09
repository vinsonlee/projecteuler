import collections
import math
import operator
import sys

import euler


def num_divisors(x):
    """
    Count number of divisors.
    """

    prime_factors = collections.defaultdict(int)

    # Find prime factors.
    while not euler.isprime(x):
        for i in range(2, int(math.ceil(math.sqrt(x))) + 1):
            if x % i == 0:
                prime_factors[i] += 1
                x = x / i
                break

    prime_factors[x] += 1
    return reduce(operator.mul, [x + 1 for x in prime_factors.values()])


i = 2
while True:
    triangle_num = i * (i + 1) / 2
    d = num_divisors(triangle_num)

    if d > 500:
        print triangle_num
        sys.exit()

    i += 1

assert False
