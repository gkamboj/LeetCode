class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet, result = set(nums), 0
        for num in numsSet:
            if num - 1 not in numsSet:
                count = 1
                while num + 1 in numsSet:
                    count += 1
                    num += 1
                result = max(result, count)
        return result
    
# Approach: https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak    