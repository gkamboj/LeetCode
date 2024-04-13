class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        l_m, r_m = height[l], height[r]
        while l < r:
            if l_m < r_m:
                l+=1
                l_m = max(height[l], l_m)
                ans += l_m - height[l]
            else:
                r -= 1
                r_m = max(r_m, height[r])
                ans += r_m - height[r]
        return ans
                
