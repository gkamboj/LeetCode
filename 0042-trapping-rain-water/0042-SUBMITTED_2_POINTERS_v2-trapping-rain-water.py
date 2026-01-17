class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans, left_max, right_max = 0, height[left], height[right]
        while left < right:
            if height[left] <= height[right]:
                area = max(0, left_max - height[left])
                left += 1
                left_max = max(left_max, height[left])
            else:
                area = max(0, right_max - height[right])
                right -= 1
                right_max = max(right_max, height[right])
            ans += area
        return ans
