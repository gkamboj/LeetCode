class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for ind in range(len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(num)
            nums.append(num)
            result += perms
        
        return result
    
# Approach: This is recursive approach. If length of input is 1, then return the list of shallow copy of input (list of list is created as it'll be used afterwards to add other elements). Now, for num in nums (by popping the num from nums), find the permutations recursively and then add it back to the list at end. Also, update the result list.
