class Solution:
    def maxArea(self, height: List[int]) -> int:
        result, start, end = 0, 0, len(height) - 1
        while start < end:
            if height[start] <= height[end]:
                result = max(result, height[start] * (end - start))
                start += 1
            else:
                result = max(result, height[end] * (end - start))
                end -= 1
        return result