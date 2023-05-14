import math as m

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        l, ans, fact = [str(i + 1) for i in range(n)], '', m.factorial(n - 1)
        k -= 1
        while n > 0:
            n -= 1
            if k == 0:
                ans += ''.join(l)
                break
            val, k = k // fact, k % fact
            fact //= n
            ans += l[val]
            l.remove(l[val])
        return ans
    
# Approach: For a given ith position, (n - i)! permutations are possible for part beyond i. For permutations of n, the first (n-1)! permutations start with 1, next (n-1)! ones start with 2, ... and so on. And in each group of (n-1)! permutations, the first (n-2)! permutations start with the smallest remaining number. When k == 0, that means remaining digits can be used as it is.

# Note-1: Observe that k -= 1 is used before while loop. This is to handle edge case when k divided (n - 1)!, (like k = 48, n = 5: we want val = 1 that is 47//4! and not 48//4! = 2). See replies to https://leetcode.com/problems/permutation-sequence/discuss/22512/Share-my-Python-solution-with-detailed-explanation/167097 for more detail.

# Note-2: Another way to understand k -= 1 is that 1st permutation is the initial list from 1 to n that is it is already given, so to find kth permutation, we need to do (k - 1) operations only.