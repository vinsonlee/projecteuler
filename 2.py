#!/usr/bin/env python

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

a = 1  # two numbers ago
b = 2  # previous number
total = 2

while True:
    fib = a + b
    if fib > 4000000:
        break
    if fib % 2 == 0:
        total += fib
    a = b
    b = fib

print total
