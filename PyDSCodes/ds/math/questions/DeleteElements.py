# Given an integer array A of size N. Find the minimum number of elements that need to be removed such that the GCD
# of the resulting array becomes 1. If not possible then return -1.

def deleteElements(arr):
    ans, gcd = -1, A[0]
    for i in A[1:]:
        gcd = self.gcd(gcd, i)
        if gcd == 1:
            ans = 0
            break
    return ans


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
