# A lucky number is a number that has exactly 2 distinct prime divisors. You are given a number A, and you need to
# determine the count of lucky numbers between the range 1 to A (both inclusive).

def luckyNumber(n):
    sieveArr = sieve(n)
    count = 0
    for i in range(2, n + 1):
        if sieveArr[i] == 2:
            count += 1
    return count


def sieve(n):
    arr = [0 for i in range(n + 1)]
    for i in range(2, n + 1):
        if arr[i] == 0:
            for j in range(i, n + 1, i):
                arr[j] += 1
    return arr


print(luckyNumber(12))

# Approach: Create a sieve to store the number of unique prime factors. Traverse over this created sieve array to get
# the desired count.
