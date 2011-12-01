f = open('names.txt')
names = f.readline()
f.close()

names = names.replace('\"', '')
names = names.split(',')
names = sorted(names)

total = 0
for i in range(len(names)):
    score = (i + 1) * sum([ord(c) - ord('A') + 1 for c in names[i]])
    total += score
print total
