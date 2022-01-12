class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        ans = (len(height) - 1) * min(height[0], height[-1])
        currArea = ans
        while start < end:
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
            currArea = (end - start) * min(height[start], height[end])
            ans = max(ans, currArea)
        return ans

#Approach: Use two pointers to start with area having max width. Go to a shorter width container only if there is a vertical line longer than the current containers shorter line. Keep in mind that for current container, lower height isn't supporting the higher water level and can thus be safely removed from further consideration.
