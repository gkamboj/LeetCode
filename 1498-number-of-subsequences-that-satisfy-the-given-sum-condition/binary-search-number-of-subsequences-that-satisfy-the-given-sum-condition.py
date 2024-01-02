class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] + nums[end] <= target:
                count = (count + (1 << (end - start))) % (10 ** 9 + 7)
                start += 1
            else:
                end -= 1
        return count % (10 ** 9 + 7)
    
# Approach: For every (start, end) pair, add all subsequences with minimum number as nums[start] to the count
