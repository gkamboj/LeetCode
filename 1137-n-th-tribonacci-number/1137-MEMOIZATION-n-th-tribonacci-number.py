class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return 1
        else:
            a, b, c = 0, 1, 1
            k = 3
            while k < n:
                s = a + b + c
                a = b
                b = c
                c = s
                k += 1
            return a + b + c
