#!/usr/bin/env python

# n answer
# 1 1
# 2 2
# 3 6
# 4 12
# 5 60
# 6 60
# 10 2520

answer = 1

for i in range(1, 20 + 1):
    for j in range(1, i + 1):
        p = answer * j
        if p % i == 0:
            answer = p
            break

print answer
