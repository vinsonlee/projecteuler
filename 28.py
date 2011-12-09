def diagonal_numbers(n):
    assert(n % 2 == 1)

    if n == 1:
        return [1]

    numbers = range((n - 2) ** 2 + 1, n ** 2 + 1)
    numbers = numbers[(n - 2)::(n - 1)]
    return numbers


total = 0
for i in range(1, 1002, 2):
    total += sum(diagonal_numbers(i))
print total
