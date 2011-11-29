#!/usr/bin/env python

import math

import euler

number = 600851475143
largest_prime_factor = 1

for i in range(2, int(math.sqrt(number)) + 1):
    if number % i == 0 and euler.isprime(i):
        largest_prime_factor = i

print largest_prime_factor
