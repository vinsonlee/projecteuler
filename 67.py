triangle = []

f = open('triangle.txt')
for line in f:
    triangle.append([int(s) for s in line.strip().split()])
f.close()

assert len(triangle) == 100

cache = {}


def maximum_total(row, index):
    assert row < len(triangle)
    assert index >= 0
    assert index <= row

    h = hash((row, index))
    if h in cache:
        return cache[h]

    if row == len(triangle) - 1:
        return triangle[row][index]

    total = triangle[row][index] + \
        max([maximum_total(row + 1, index),
             maximum_total(row + 1, index + 1)])
    cache[h] = total
    return total


print maximum_total(0, 0)
