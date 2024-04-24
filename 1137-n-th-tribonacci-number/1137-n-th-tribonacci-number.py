class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return 1
        else:
            arr = [0, 1, 1]
            while len(arr) < n + 1:
                arr.append(arr[-1] + arr[-2] + arr[-3])
            return arr[-1]