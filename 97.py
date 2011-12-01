answer = 1
for i in range(7830457):
    answer *= 2
    answer = answer % (10 ** 10)

print (28433 * answer + 1) % (10 ** 10)
