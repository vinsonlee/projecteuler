N = 100
terms = []

for a in range(2, N + 1):
    for b in range(2, N + 1):
        terms.append(a ** b)

print len(sorted(list(set(terms))))
