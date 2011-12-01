import itertools
import string

i = 0
for p in itertools.permutations(string.digits):
    i += 1
    if i == 1000000:
        answer = p
        break

print ''.join(answer)
