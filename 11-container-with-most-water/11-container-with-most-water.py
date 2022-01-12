class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        currStart, currEnd = height[0], height[end]
        ans = (len(height) - 1) * min(currStart, currEnd)
        currArea = ans
        while start < end:
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
            if height[end] > currEnd or height[start] > currStart:
                currArea = (end - start) * min(height[start], height[end])
                currStart, currEnd = height[start], height[end]
            ans = max(ans, currArea)
        return ans