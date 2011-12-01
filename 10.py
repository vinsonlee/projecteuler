N = 2000000

# Sieve of Eratosthenes
# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

# boolean array for primes
# n is prime if primes[n] is True
primes = [True] * N
primes[0] = False
primes[1] = False

p = 2
while p * p <= N:
    # Mark all multiples of p as non-prime.
    for i in xrange(p * p, len(primes), p):
        primes[i] = False

    # Find the next prime.
    for i in xrange(p + 1, len(primes)):
        if primes[i]:
            p = i
            break

total = 0
for i in xrange(len(primes)):
    if primes[i]:
        total += i

print total
