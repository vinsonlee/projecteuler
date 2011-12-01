N = 1000000

# Cache of Collatz results.
C = {}
C[1] = 1


def collatz(x):
    """
    Calculate the number of terms for the sequence starting with x.
    """
    if x in C:
        return C[x]
    elif x % 2 == 0:
        answer = 1 + collatz(x / 2)
    else:
        answer = 1 + collatz(3 * x + 1)

    C[x] = answer
    return answer

longest_chain = 1
starting_number = 1

for i in range(2, N):
    chain = collatz(i)
    if chain > longest_chain:
        longest_chain = chain
        starting_number = i

print starting_number
