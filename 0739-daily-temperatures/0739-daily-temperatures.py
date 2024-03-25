class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result, stack = [0 for i in range(len(temperatures))], []
        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][-1] < temp:
                top_ind = stack.pop()[0]
                result[top_ind] = ind - top_ind
            stack.append([ind, temp])
        return result