class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [[nums[0]]]
        
        for ind in range(1, len(nums)):
            temp = []
            for combo in ans:
                temp += self.helper(combo, nums[ind])
            ans = list(temp)
        
        return ans

    def helper(self, arr, num):
        result = []
        for i in range(len(arr) + 1):
            result.append(arr[:i] + [num] + arr[i:])
        return result