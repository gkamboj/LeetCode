class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            perms = []
            for perm in ans:
                for i in range(len(perm) + 1):
                    perms.append(perm[:i] + [num] + perm[i:])
            ans = perms
        return ans