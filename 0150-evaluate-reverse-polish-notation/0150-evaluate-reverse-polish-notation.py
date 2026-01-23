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
                        val = int(scLast/last)
                result.append(val)
            else:
                result.append(int(token))
        return result[-1]
        