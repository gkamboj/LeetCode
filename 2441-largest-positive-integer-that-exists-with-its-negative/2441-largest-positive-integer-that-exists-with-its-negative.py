class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        covered, ans = set(), -1
        for num in nums:
            if -num in covered:
                ans = max(abs(num), ans)
            else: covered.add(num)
        return ans
                
'''
Approach: similar to approach-4
'''