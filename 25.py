import sys

a = 1  # F(n-2)
b = 1  # F(n-1)
n = 3  # term number

while True:
    fib = a + b

    if len(str(fib)) == 1000:
        print n
        sys.exit()

    a = b
    b = fib
    n += 1

assert False
