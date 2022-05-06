class Solution:
    def grayCode(self, n: int) -> List[int]:
        start, result = 1, [0]
        while start <= n:
            result += [i | (1 << (start - 1)) for i in reversed(result)]
            start += 1
        return result
    
# Approach: This is an iterative approach. Use the fact that for every 2^n gray codes, next 2^n gray codes can be found by adding 2^n to each value (in reverse order). For. eg.,:

# n = 0 =>   0 (0)
# n = 1 =>   1 (1)
# n = 2 =>  11 (3)
#           10 (2)
# n = 3 => 110 (6)
#          111 (7)
#          101 (5)
#          100 (4)
