class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    stack.pop()
                    continue # if there is a collision, we should continue to avoid breaking after this iteration.
                elif stack[-1] == -ast:
                    stack.pop()
                break
            else: # else will always be called after while if while loop ends naturally (that is without break)
                stack.append(ast)
        return stack

'''
Approach: Use a stack to keep surviving asteroids. For each incoming asteroid, 
repeatedly check collisions with the top of the stack (only when top is positive and 
incoming is negative), popping smaller ones. If the incoming asteroid survives all 
collisions, append it to the stack.
'''
