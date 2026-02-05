class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n != 1:
            curr = 0
            while n:
                curr += (n % 10) ** 2
                n //= 10
            if curr in nums:
                return False
            nums.add(curr)
            n = curr

        return True

# Approach: Maintain a set of visited numbers and continue till either a number is repeated or we reach 1.
