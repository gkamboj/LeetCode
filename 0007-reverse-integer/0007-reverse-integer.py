class Solution:
    def reverse(self, x: int) -> int:
        ans, max_val = 0, 2 ** 31
        neg = -1 if x < 0 else 1
        x = abs(x)
        while x:
            rem = x % 10
            x //= 10
            if (ans > max_val / 10) or (ans == max_val // 10 and rem > max_val % 10):
                return 0
            ans  = (ans * 10) + rem
            
        return ans * neg

# Approach: Mathematical algo to revser number. To handle 32 bit constraint, check that updated ans should not be more than
# max_val (2^31) before actually making the update.