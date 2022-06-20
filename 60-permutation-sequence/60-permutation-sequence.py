import math as m

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        l, ans = [str(i + 1) for i in range(n)], ''
        k -= 1
        while n > 0:
            n -= 1
            val, k = k // m.factorial(n), k % m.factorial(n)
            ans += l[val]
            l.remove(l[val])
        return ans