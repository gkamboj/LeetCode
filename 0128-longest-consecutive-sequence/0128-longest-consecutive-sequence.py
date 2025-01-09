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