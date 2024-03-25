class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        l_max, r_max, ans = height[left], height[right], 0
        while left < right:
            if l_max < r_max:
                left += 1
                val = height[left]
                l_max = max(l_max, val)
            else:
                right -= 1
                val = height[right]
                r_max = max(r_max, val)
            ans += max(min(l_max, r_max) - val, 0)
        return ans
                            
        