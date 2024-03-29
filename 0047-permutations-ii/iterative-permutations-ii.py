class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for num in nums:
            perms = []
            for perm in result:
                for i in range(len(perm) + 1):
                    perms.append(perm[:i] + [num] + perm[i:])
                    if i < len(perm) and perm[i] == num:
                        break
            result = perms
        
        return result
                
                    
        
# Approach: This is iterative approach similar to LC-46. To handle duplicates, dont't add a number after its duplicate (as permutations arising from this will aready be taken care from other cases).
