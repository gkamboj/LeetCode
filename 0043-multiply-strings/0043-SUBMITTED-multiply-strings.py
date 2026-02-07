class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num2 == "0" or num1 == "0":
            return "0"
        
        ans, carry = ["0" for i in range(len(num1) + len(num2))], 0

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                val = int(num1[i]) * int(num2[j]) + carry + int(ans[i + j + 1])
                ans[i + j + 1] = str(val % 10)
                carry = val // 10
            ans[i] = str(int(ans[i]) + carry)
            carry = 0
        ans[0] = str(int(ans[0]) + carry)

        return str(int("".join(ans)))

# Approach: Programming way of how we do multiplication on paper. See below examples to understand
# how nested loop in code works.

#     1 2 3
#     4 5 6
# ----------
#     7 3 8
#   6 1 5 x
# 4 9 2 x x
# ----------
# 5 6 0 8 8
# ----------

#     4 5 6
#     1 2 3
# ----------
#   1 3 6 8
#   9 1 2 x
# 4 5 6 x x
# ----------
# 5 6 0 8 8
# ----------
