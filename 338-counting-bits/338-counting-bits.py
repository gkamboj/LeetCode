class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for i in range(n + 1)]
        for i in range(32):
            for n in range(1, n + 1):
                ans[n] += (n >> i) & 1
        return ans

#Approach: For every ith bith from 0 to 31, check set bits and add to corresponding array index element.

#Here using more than single pass. Refer other submission for optimized approach with single pass.