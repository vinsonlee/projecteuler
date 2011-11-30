#!/bin/env

import euler

largest_palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if product > largest_palindrome and euler.ispalindrome(product):
            largest_palindrome = product

print largest_palindrome
