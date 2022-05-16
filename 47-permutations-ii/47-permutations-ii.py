from collections import defaultdict

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