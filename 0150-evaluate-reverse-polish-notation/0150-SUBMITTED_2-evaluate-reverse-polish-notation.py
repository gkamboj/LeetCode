class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except:
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
                            res = int(v1 / v2)
                stack.append(res)
        return stack.pop()

'''
Approach: Similar to other SUBMITTED approach, except that it uses EAFP.
'''
