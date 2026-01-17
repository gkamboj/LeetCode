class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, left, right = 0, 0, len(height) - 1
        while left < right:
            left_ht, right_ht = height[left], height[right]
            ans = max(ans, min(left_ht, right_ht) * (right - left))
            if left_ht < right_ht:
                left += 1
            else:
                right -= 1
        return ans
