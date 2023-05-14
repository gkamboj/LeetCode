class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        absx = abs(x)
        while absx > 0:
            ans = ans * 10 + absx % 10
            absx //= 10
        if ans > 2 ** 31 - 1:
            return 0
        if x < 0:
            ans *= -1
        return ans
    
#Approach: Reversing part is self-explanatory. For overflow part, comparison with (2 ** 31 - 1) has been done because Python does not have overflow concept. But this approach will fail in Java. For Java, check after every iteration if current value is overflown by doing similar to https://leetcode.com/problems/reverse-integer/discuss/4060/My-accepted-15-lines-of-code-for-Java 