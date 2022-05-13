class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [1 for i in range(n)]
        for row in range(1, m):
            for col in range(1, n):
                arr[col] += arr[col - 1]
        return arr[-1]
    
# Approcah: This is DP approach using 1-D array. This follows same logic as other DP submission but using 1-D array only. Observe that at any time, we need to access just the left and top element and that can be done using 1-D array only: left element is preceding element and top element is just the current value at current index. See explanation of 2-D DP submission for more detail on logic.