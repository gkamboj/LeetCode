# Given an integer array A of size N. Find the minimum number of elements that need to be removed such that the GCD
# of the resulting array becomes 1. If not possible then return -1.

def deleteElements(arr):
    gcdVal = arr[1]
    for num in arr[1:]:
        gcdVal = gcd(gcdVal, num)
    if gcdVal > 1:
        return -1
    else:
        return 0


def gcd(a, b):
    while b > 0:
        rem = b % a
        a = b
        b = rem
    return a


print(deleteElements([9, 3, 6]))

# Approach: Observe that after removing any element from the array, GCD will always increase or remain same but it'll
# never decrease. So, if GCD of the array is already 1 then minimum number of elements to be removed is 0,
# but if GCD > 1, then it's not possible to make it 1.
