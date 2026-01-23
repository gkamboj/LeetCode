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
                result.append(val)
            else:
                result.append(int(token))
        return result[-1]
        