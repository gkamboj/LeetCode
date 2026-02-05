class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.squaresSum(n)
        while slow != fast:
            slow = self.squaresSum(slow)
            fast = self.squaresSum(self.squaresSum(fast))
        return slow == 1

    def squaresSum(self, n):
        ans = 0
        while n:
            ans += (n % 10) ** 2
            n //= 10
        return ans