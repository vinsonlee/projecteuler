#!/usr/bin/env python


def sum_of_squares(n):
    """
    Return the sum of the squares of the first n natural numbers.
    """
    return sum([x ** 2 for x in range(1, n + 1)])


def square_of_sum(n):
    """
    Return the square of the sum of the first n natual numbers.
    """
    return sum(range(1, n + 1)) ** 2


N = 100

print square_of_sum(N) - sum_of_squares(N)
