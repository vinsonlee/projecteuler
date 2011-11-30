#!/usr/bin/env python

import euler

num_primes = 0
number = 1

while num_primes != 10001:
    if euler.isprime(number):
        last_prime = number
        num_primes += 1
    number += 1

print last_prime
