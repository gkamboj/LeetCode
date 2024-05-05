class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target: end = mid - 1
            else: start = mid + 1
        return -1
    
'''
Approach: Implementation of Binary Search. Do check LC Binary Search explore card for more conceptual
understanding: https://leetcode.com/explore/learn/card/binary-search/
'''
