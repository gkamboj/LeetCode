# Given an even number A ( greater than 2 ), return two prime numbers whose sum will be equal to the given number. If
# there is more than one solution possible, return the lexicographically smaller solution.

def primeSum(n):
    sieveArr = sieve(n)
    for i in range(2, n // 2 + 1):
        if sieveArr[i] == 0 and sieveArr[n - i] == 0:
            return [i, n - i]


def sieve(n):
    arr = [0 for i in range(n + 1)]
    for i in range(2, n + 1):
        if arr[i] == 0:
            for j in range(i * i, n + 1, i):
                arr[j] = 1
    return arr


print(primeSum(16))

# Approach: Prepare a sieve to store every prime number till n, and traverse over sieve array to check combination of
# (i, n - i) s.t. both i and (n - i) are prime numbers.
