class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack, operators = [], ['+', '-', '*', '/']
        for val in tokens:
            if val not in operators:
                stack.append(int(val))
            else:
                self.calculate(stack, val)
        return stack.pop()
            
    def calculate(self, stack, val):
        op1, op2 = stack.pop(), stack.pop()
        match val:
            case '+':
                stack.append(op1 + op2)
            case '-':
                stack.append(op2 - op1)
            case '*':
                stack.append(op2 * op1)
            case '/':
                stack.append(self.divide(op2, op1))
                
    def divide(self, a, b):
        if a * b <= 0:
            return -(abs(a)//abs(b))
        else:
            return a//b
                
                
                