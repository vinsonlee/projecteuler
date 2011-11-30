#!/usr/bin/env python

import sys

for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = 1000 - a - b

        if c < 1:
            continue

        if c <= b:
            continue

        assert a + b + c == 1000

        if a ** 2 + b ** 2 == c ** 2:
            print a * b * c
            sys.exit()

assert False
