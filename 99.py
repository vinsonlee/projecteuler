import math

# if a > b
# then log(a) > log(b)
#
# log(a ** x) == x * log(a)

lines = 0
greatest_value = 0

f = open('base_exp.txt')

for line in f:
    lines += 1
    (base, exp) = [int(s) for s in line.split(',')]
    value = exp * math.log(base)

    if value > greatest_value:
        greatest_value = value
        line_number = lines

f.close()

print line_number
