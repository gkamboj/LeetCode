class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num2 == "0" or num1 == "0":
            return "0"
        
        n1 = max(int(num1), int(num2))
        n2 = min(int(num1), int(num2))

        ans = 0
        while n2:
            if n2 & 1:
                ans += n1
            n2 >>= 1
            n1 *= 2
        
        return str(ans)

# Approach: Keep doubling the higher number and halving the smaller number. Add the higher number to `ans` whenever the smaller number becomes odd.

# NOTE: This approach is NOT ALLOWED AS INPUT CANNOT BE CONVERTED TO INTEGER DIRECTLY as per the given constraints. It's done just for conceptual understanding.
