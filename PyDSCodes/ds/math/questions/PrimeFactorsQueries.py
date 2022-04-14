# You are given A queries. For each query (1<=i<=A) you are given a prime number B[i], you need to give the count of
# all numbers in range 1 to 10^6 inclusive which have minimum prime factor B[i] for each query.

def primeFactorsQueries(arr):
    sieveDict = sieve(1000000)
    result = []
    for num in arr:
        result.append(sieveDict[num])
    return result


def sieve(n):
    arr = [i for i in range(n + 1)]
    dict = {}
    for i in range(2, n + 1):
        if arr[i] == i:
            dict[i] = 1
            for j in range(i * i, n + 1, i):
                if arr[j] == j:
                    arr[j] = i
                    dict[i] += 1
    return dict


print(primeFactorsQueries([13, 17]))

# Approach: Since there are multiple queries, it's better to store information for every number till 10^6 instead of
# computing it for every query. This can be done through Sieve. Also, while computing sieve dictionary can be used
# instead of traversing over sieve array for every query. Remember to check if number is already modified or not
# inside inner loop before increasing the count (line-18).
