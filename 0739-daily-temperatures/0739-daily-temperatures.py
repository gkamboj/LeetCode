class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, ans = [], [0 for i in range(len(temperatures))]
        for ind, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                topTemp, topInd = stack.pop()
                ans[topInd] = (ind - topInd)
            stack.append((temp, ind))
        return ans
