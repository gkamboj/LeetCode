class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        
        left, right, prod = 0, 0, 1
        ans = 0
        
        while right < len(nums):
            prod *= nums[right]
            
            while prod >= k:
                prod //= nums[left]
                left += 1
            
            ans += right - left + 1
            right += 1
        
        return ans