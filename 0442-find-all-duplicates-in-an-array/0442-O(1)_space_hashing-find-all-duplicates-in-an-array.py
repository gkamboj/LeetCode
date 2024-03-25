class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            abs_num = abs(num)
            if nums[abs_num - 1] < 0:
                ans.append(abs_num)
            else:
                nums[abs_num - 1] *= -1
        return ans
    
# Approach: Use input array itself as hash to store visited numbers as negative. Once we encounter a negative value,
# add that value to ans array as that is already visited.
