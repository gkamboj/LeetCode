# You are given 2 arrays A and B of size N and M respectively and a number K. You have to tell that how many pairs (
# A[i], B[j]) (1 <= i <= N and 1 <= j <= m) exists such that product of them is not CoPrime with K.

def coprimeAgain(arr1, arr2, k):
    arr1Coprimes, arr2Coprimes = 0, 0
    for num in arr1:
        if gcd(num, k) == 1:
            arr1Coprimes += 1
    for num in arr2:
        if gcd(num, k) == 1:
            arr2Coprimes += 1
    return len(arr1) * len(arr2) - arr1Coprimes * arr2Coprimes


def gcd(a, b):
    while b > 0:
        rem = a % b
        a = b
        b = rem
    return a


print(coprimeAgain([1, 2, 3, 3], [1, 2, 3, 4, 5], 3))

# Approach: Traverse over both arrays one by one to store the count of elements which are coprime with k. Subtract
# multiplication of this count from total possible pairs to get the answer.
