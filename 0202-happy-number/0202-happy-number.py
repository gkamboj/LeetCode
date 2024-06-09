class Solution:
    def isHappy(self, n: int) -> bool:
        vals = []
        while True:
            temp = 0
            while n:
                temp += (n % 10) ** 2
                n = n // 10
            if temp in vals:
                return False
            elif temp == 1:
                return True
            else:
                n = temp
                vals.append(temp)