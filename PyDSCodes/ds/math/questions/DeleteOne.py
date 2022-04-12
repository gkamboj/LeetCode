# Given an integer array A of size N. You have to delete one element such that the GCD of
# the remaining array is maximum. Find the maximum value of GCD.

def deleteOne(arr):
    prefixGcds = [num for num in arr]
    suffixGcds = [num for num in arr]
    for i in range(1, len(arr)):
        prefixGcds[i] = gcd(prefixGcds[i - 1], arr[i])
        suffixGcds[-1 * (i + 1)] = gcd(arr[-1 * (i + 1)], suffixGcds[-1 * i])
    ans = max(suffixGcds[1], prefixGcds[len(arr) - 2])
    for i in range(1, len(arr) - 1):
        ans = max(ans, gcd(prefixGcds[i - 1], suffixGcds[i + 1]))
    return ans


def gcd(a, b):
    while b > 0:
        rem = a % b
        a = b
        b = rem
    return a


print(deleteOne([5, 15, 30]))

# Approach: Create 2 new arrays to store the prefix and suffix GCDs. These 2 arrays can be used to find the GCD of
# given array after omitting any index i by finding GCD(prefix[i - 1], suffix[i + 1]). Do this for every index and
# return the maximum value. 
