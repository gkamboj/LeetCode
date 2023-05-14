class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.subsetsRecursively(nums, [], result)
        return result
    
    def subsetsRecursively(self, nums, subset, result):
        result.append(subset)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.subsetsRecursively(nums[i + 1:], subset + [nums[i]], result)
            
# Approach: This is recursive approach similar to LC-78 DFS submission. To handle duplicates, pass the sorted input in recursive method and on encountering 2nd (or any subsequent) instance of any element, ignore recursive call (because all related subsets for that element would already be created in previous calls)

# Note: This approach will give sorted and lexicographic result.
