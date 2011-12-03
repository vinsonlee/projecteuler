total = 0

for i in range(1, 10 ** 6):
    dec_string = str(i)
    bin_string = bin(i).split('0b')[1]

    if dec_string == dec_string[::-1] and bin_string == bin_string[::-1]:
        total += i

print total
