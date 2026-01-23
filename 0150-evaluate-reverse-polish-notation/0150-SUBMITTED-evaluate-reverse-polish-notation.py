class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result, operators = [], ['+', '-', '*', '/']
        for token in tokens:
            if token in operators:
                last, scLast = result.pop(), result.pop()
                match token:
                    case '+':
                        val = scLast + last
                    case '-':
                        val = scLast - last
                    case '*':
                        val = scLast * last
                    case '/':
                        negMultiplier = -1 if scLast * last < 0 else 1
                        val = abs(scLast) // abs(last) * negMultiplier
                        # This can also be done easily as int(scLast/last)
                result.append(val)
            else:
                result.append(int(token))
        return result[-1]

# Approach: Keep pushing non-operator tokens to the stack, and pop the top two whenever a token is an operator.
# Remember to handle division of negatives as it has to be truncated towards zero.
