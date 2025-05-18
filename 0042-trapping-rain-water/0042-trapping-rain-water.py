class Solution:
    def trap(self, height: List[int]) -> int:
        arr = [0 for i in range(len(height))]
        ans, l_max, r_max = 0, height[0], height[-1]
        for ind in range(len(height) - 1, -1, -1):
            r_max = max(r_max, height[ind])
            arr[ind] = r_max
        for ind in range(len(height) - 1):
            ans += max(min(l_max, arr[ind + 1]) - height[ind], 0)
            l_max = max(l_max, height[ind])
        return ans

# Approach: Create an array to store maximum value from right at any index. Then traverse
# and keep adding the water that can be stored due to current index.