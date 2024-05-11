class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            mid_val = self.get_mid_val(nums[0], nums[mid], target)
            if mid_val == target:
                return mid
            elif mid_val > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    
    
    def get_mid_val(self, start_val, mid_val, target):
        ans = mid_val
        # Using >= and not > because "=" and ">" cases corresponds to part after pivot, "<" to part before
        # We are checking if mid_val and target are on opposite sides of pivot
        if mid_val >= start_val and target < start_val:
            ans = -10**4 - 1
        elif mid_val < start_val and target >= start_val:
            ans = 10**4 + 1
        return ans
    
'''
Approach: https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple
'''