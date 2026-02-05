class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n != 1:
            curr = 0
            while n > 0 :
                curr += (n % 10) ** 2
                n //= 10
            if curr in nums:
                return False
            nums.add(curr)
            n = curr

        return True