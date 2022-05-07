class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        count = [0]
        self.numSquarefulRecursive(sorted(nums), [], count)
        return count[0]
    
    def numSquarefulRecursive(self, nums, perm, count):
        if not nums:
            count[0] += 1
            
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if not perm or (perm and self.isPerfectSquare(perm[-1] + nums[i])):
                self.numSquarefulRecursive(nums[:i] + nums[i + 1:], perm + [nums[i]], count)
        
    def isPerfectSquare(self, num):
        return int(num ** 0.5) ** 2 == num
    
# Approach: This is recursive DFS solution. To handle duplicate permutations, pass sorted input to recursive method and check if current num is not equal to its previous, only then call the recursive method. For every element, check if its sum with last element of perm is perfect square. If so, call the recursive method again after omitting it from array.

# Reference: https://leetcode.com/problems/number-of-squareful-arrays/discuss/841254/Python-easy-to-understand-backtracking-solution-with-comments
