class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result, stack = [0 for i in range(len(temperatures))], []
        for ind, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                top_ind = stack.pop()
                result[top_ind] = ind - top_ind
            stack.append(ind)
        return result
    
# Approach: Using stack, store currently unsolved elements. When encountered higher temp, pop all smaller temps
# and update the answer. Solve more problems on monotonic stack for better clarity: https://www.notion.so/Stacks-d0ba7936119243e0993895078b96ebaf?pvs=4
