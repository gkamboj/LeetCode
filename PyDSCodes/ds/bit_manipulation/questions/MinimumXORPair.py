# Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. Report
# the minimum XOR value.

def minXORPair(arr):
    arr.sort()
    ans = arr[0] ^ arr[1]
    for ind in range(2, len(arr)):
        ans = min(ans, arr[ind] ^ arr[ind - 1])
    return ans


print(minXORPair([0, 4, 7, 9]))

# Approach: Sort the array and take XOR of every consecutive pair. The minimum of these will be the answer. This is
# because for any 3 numbers a, b, c s.t. a < b < c, min XOR will be either (a, b) or (b, c), but never (a, c). To prove
# this, let's consider the leftmost bits of a, b, c. Two cases are possible:
# 1. Leftmost bits: (a, b, c) = (0, 1, 1) => Leftmost bits of XOR: a^b = 1, b^c = 0, a^c = 1 => minimum = b^c
# 2. Leftmost bits: (a, b, c) = (0, 0, 1) => Leftmost bits of XOR: a^b = 0, b^c = 1, a^c = 1 => minimum = a^b
# Above cases prove minimum will always be from consecutive pair.
