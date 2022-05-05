class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        for i in range(1 << n):
            result.append(i ^ (i // 2))
        return result
    
# Approach: G(i) = i ^ (i / 2)

# Reference: https://leetcode.com/problems/gray-code/discuss/29881/An-accepted-three-line-solution-in-JAVA
