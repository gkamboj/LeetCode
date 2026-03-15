class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        self.fun(nums, ans)
        return ans

    def fun(self, nums, ans):
        if not nums:
            return
        num = nums[0]
        for ind in range(len(ans)):
            new_val = ans[ind][:]
            new_val.append(num)
            ans.append(new_val)
        self.fun(nums[1:], ans)
        