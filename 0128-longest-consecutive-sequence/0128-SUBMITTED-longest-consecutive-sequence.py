class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st, ans = set(nums), 0
        for num in st:
            curr = 1
            if (num - 1) not in st:
                while (num + 1) in st:
                    curr += 1
                    num += 1
                ans = max(ans, curr)
        return ans
    
# Approach: https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak  
# Same approach can also be done using Dictionary/Map.

# Notes:
# 1. Line-4 -> for loop should be on st insead of st to reduce the extra iterations due to duplicates. LC gives TLE if nums is used.
# 2. Line-3 -> ans should be initialized to 0, not 1. Initialising it to 1 will result in failure of [] case.
