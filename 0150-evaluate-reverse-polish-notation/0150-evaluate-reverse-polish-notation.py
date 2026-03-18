class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                v2, v1 = stack.pop(), stack.pop()
                match token:
                    case '+':
                        res = v1 + v2
                    case '*':
                        res = v1 * v2
                    case '-':
                        res = v1 - v2
                    case '/':
                        if v1 * v2 > 0:
                            res = v1 // v2
                        else:
                            res = math.ceil(v1 / v2)
                stack.append(res)
        return stack.pop()