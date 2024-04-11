class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums, val = list(num), k
        n = len(nums)
        if n <= k: return '0'
        stack, ind = [], 0
        while ind < n:
            while stack and stack[-1] > nums[ind] and val:
                stack.pop()
                val -= 1
            stack.append(nums[ind])
            ind += 1
        sys.set_int_max_str_digits(max(n - k + 1, 640))
        return str(int(''.join(stack[:n-k])))
