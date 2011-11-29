#!/usr/bin/env python

# 9! = 362880
# 7 * 9! = 2540160
# 8 * 9! = 2903040
#
# The maximum sum would be 2540160.

import math

N = 2540160
total = 0

for i in range(10, N + 1):
    s = sum([math.factorial(int(c)) for c in str(i)])
    if s == i:
        total += i

print total
