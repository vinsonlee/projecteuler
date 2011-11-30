#!/usr/bin/env python

import math


def C(n, r):
    assert r <= n
    return math.factorial(n) / math.factorial(r) / math.factorial(n - r)


values = 0

for n in range(1, 100 + 1):
    for r in range(1, n):
        c = C(n, r)
        if c > 1000000:
            values += 1

print values
