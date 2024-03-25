class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, ans = 0, len(height) - 1, 0
        l_max, r_max = height[left], height[right]
        while left < right:
            if l_max > r_max:
                right -= 1
                r_max = max(r_max, height[right])
                ans += r_max - height[right]
            else:
                left += 1
                l_max = max(l_max, height[left])
                ans += l_max - height[left]
        return ans
                
# Approach: Use 2 pointers to store left max and right max. Detail: https://www.youtube.com/watch?v=ZI2z5pq0TqA