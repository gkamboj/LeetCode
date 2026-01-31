class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            mid_val = self.get_mid_val(nums[start], nums[mid], target)
            if mid_val == target:
                return mid
            elif mid_val > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    
    
    def get_mid_val(self, start_val, mid_val, target):
        ans = mid_val
        if mid_val >= start_val and target < start_val:
            ans = -10**4 - 1
        elif mid_val < start_val and target >= start_val:
            ans = 10**4 + 1
        return ans
