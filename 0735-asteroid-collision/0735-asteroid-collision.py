class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            add_ast = True
            if stack:
                while stack and stack[-1] > 0 and ast < 0:
                    if abs(ast) > abs(stack[-1]):
                        stack.pop()
                    elif abs(ast) == abs(stack[-1]):
                        stack.pop()
                        add_ast = False
                        break
                    else:
                        add_ast = False
                        break
                if add_ast:
                    stack.append(ast)
            else:
                stack.append(ast)
        return stack