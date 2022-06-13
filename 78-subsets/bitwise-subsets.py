class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(1 << len(nums)):
            subset = []
            for j in range(len(nums)):
                if (i >> j) & 1 == 1:
                    subset.append(nums[j])
            result.append(subset)
        return result
    
# Approach: This is bitwise approach. We know that for array of size n, 2^n subsets exists. So for every number from 0 to (2^n - 1), consider the set bits and form subset of elements present at those set bits. As every number has unique binary representation, we'll get unique subsets at the end.

# TC: n * 2^n (more time than recursive approach)

# Note: This approach will give sorted and lexicographic result if (sorted if input array is sorted)
