class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for num in nums:
            perms = []
            for perm in result:
                for i in range(len(perm) + 1):
                    perms.append(perm[:i] + [num] + perm[i:])
            result = perms
            
        return result