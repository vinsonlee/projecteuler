import math

import euler

N = 10 ** 8

sums = []
for i in xrange(1, int(math.sqrt(N))):
    for j in xrange(i + 1, int(math.sqrt(N)) + 1):
        s = sum([x ** 2 for x in xrange(i, j + 1)])

        if s >= N:
            break

        if euler.ispalindrome(s):
            sums.append(s)

print sum(set(sums))
