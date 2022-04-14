# Given an array of integers A, find and return the count of divisors of each element of the array. The order of the
# resultant array should be the same as the input array.

def countOfDivisors(arr):
    n = max(arr)
    sieveArr = sieve(n)
    result = []
    for num in arr:
        count = 1
        while num > 1:
            factor = sieveArr[num]
            factorCount = 0
            while num % factor == 0:
                num //= factor
                factorCount += 1
            count *= (factorCount + 1)
        result.append(count)
    return result


def sieve(n):
    arr = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if arr[i] == i:
            for j in range(i * i, n + 1, i):
                if arr[j] == j:
                    arr[j] = i
    return arr


print(countOfDivisors([8, 9, 10]))

# Approach: Store smallest prime factor for every number upto n (where n = max(arr)) using sieve. Also,
# if N = (f1^p1) * (f2^p2) * ..., number of factors = (p1 + 1) * (p2 + 1) *.... Using the sieve array and number of
# factors formula, required information can be found out for every element of array.
