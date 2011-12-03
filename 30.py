# 9^5 = 59049
# 9^5 * 6 = 354294
# 9^5 * 7 = 413343

total = 0

for i in range(2, 354294 + 1):
    s = sum([int(c) ** 5 for c in str(i)])
    if s == i:
        total += i

print total
