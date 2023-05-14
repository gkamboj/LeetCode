class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        suffixProduct, prefixProduct = nums[-1], nums[0]
        ans = max(suffixProduct, prefixProduct)
        
        for i in range(1, len(nums)):
            if prefixProduct == 0: prefixProduct = 1
            if suffixProduct == 0: suffixProduct = 1
            
            suffixProduct *= nums[len(nums) - i - 1]
            prefixProduct *= nums[i]
            
            ans = max(ans, prefixProduct, suffixProduct)
        
        return ans

#This is two-pointer approach to store prefix product and suffix product. If there are odd negatives or there is zero present in array, then consider maximum from both variables.
        
#See other submissions for more approaches
