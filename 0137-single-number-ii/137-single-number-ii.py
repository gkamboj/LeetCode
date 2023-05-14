class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans, negs = 0, 0
        for i in range(len(nums)):
            negs += int(nums[i] < 0)
            nums[i] = abs(nums[i])
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            ans |= ((count % 3) << i)
        return -1 * ans if negs % 3 else ans
            