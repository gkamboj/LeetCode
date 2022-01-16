class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for n in range(1, n + 1):
            ans.append(ans[n >> 1] + (n & 1))
        return ans

#Approach: DP based solution. For any n, number of set bits is a + b where a = number of set bits in n>>1 i.e. all bits except rightmost bit and b = n & 1 i.e. b = 1 if rightmost bit is set else 0.
#Refer other submission for alternative approach.
