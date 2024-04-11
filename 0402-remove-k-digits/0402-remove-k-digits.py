class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums, val = list(num), k
        n = len(nums)
        if n < k: return '0'
        stack, ind, ans = [], 0, ''
        while ind < n:
            while stack and stack[-1] > nums[ind] and val:
                stack.pop()
                val -= 1
            stack.append(nums[ind])
            ind += 1
        for digit in stack[:n-k]:
            ans += digit
        return ans.lstrip('0') or str('0')