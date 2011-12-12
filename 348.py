import collections
import math

import euler

# Trial and error until we find the 5 numbers.
N = 10 ** 9

I = int(round(math.sqrt(N)))
J = int(round(N ** (1 / 3.0)))

S = collections.defaultdict(list)

# Generate all combinations of i^2 + j^3 <= N.
# Save away all the palindromes.
for i in range(2, I + 1):
    for j in range(2, J + 1):
        n = i ** 2 + j ** 3
        if euler.ispalindrome(n):
            S[n].append((i, j))

palindromes = []

for key in S.keys():
    if len(S[key]) == 4:
        palindromes.append(key)

assert len(palindromes) == 5
print sum(palindromes)
