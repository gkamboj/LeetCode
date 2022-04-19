# Given an array of integers A of size N containing GCD of every possible pair of elements of another array. Find and
# return the original numbers used to calculate the GCD array in any order. For example, if input is {2, 2, 2, 2, 8,
# 2, 2, 2, 10}. then output will be {2, 8, 10}
from collections import defaultdict


def allGCDPair(arr):
    result = []
    arr.sort(reverse=True)
    elementMap = defaultdict(int)

    for num in arr:
        elementMap[num] += 1

    ind = 0

    while len(result) <= (len(arr) ** 0.5) - 1 and ind < len(arr):
        if elementMap[arr[ind]] > 0:
            elementMap[arr[ind]] -= 1
            for num in result:
                gcdVal = gcd(num, arr[ind])
                elementMap[gcdVal] -= 2
            result.append(arr[ind])
        ind += 1

    return result


def gcd(a, b):
    while b > 0:
        rem = a % b
        a = b
        b = rem
    return a


arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 7, 10, 12, 2, 2]
arr3 = [46, 1, 2, 1, 1, 1, 5, 45, 1, 1, 2, 5, 1, 40, 1, 1, 1, 1, 1, 1, 1, 1, 1, 31, 1]

print(allGCDPair(arr))
print(allGCDPair(arr3))

# Approach: For input of size n ** 2, output array will be of size n. Observe that maximum element of the input array
# will always be the part of output because maximum HCF will occur when maximum element HCF is taken with itself.
# Extending the similar approach for whole array, sort the array in reverse order and store the count of every
# element in map. Now traverse over the sorted array, for every iteration if current element frequency is greater than
# 1, append it to result and decrease the frequency by 1 in map (because current element is maximum => it should be
# part of output array). Also, before appending it to result, find GCD of element with all existing elements of result
#  one by one and decrement the frequency of resulting GCDs by 2 (because every GCD of non-self pair will occur twice:
#  GCD(a, b) = GCD(b, a))
#
# Below is the summary of the steps:
# 1. Sort the array in decreasing order.
# 2. Highest element will always be one of the original numbers. Keep that number and remove it from the array.
# 3. Compute GCD of the element taken in the previous step with the current element starting from the greatest and
# discard the GCD value from the given array
