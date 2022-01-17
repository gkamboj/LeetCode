class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1
            n = n & (n - 1)
        return count

#Approach: n & (n - 1) unsets the rightmost set bet of n. So, keep unsetting rightmost bits till every bit unsets (and hence n becomes zero). TC -> O(no. of set bits)

#See other submission of O(N) approach