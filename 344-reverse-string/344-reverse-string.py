class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s))
        
    def reverse(self, s, ind, n):
        if ind >= n // 2:
            return
        s[ind], s[n - ind - 1] = s[n - ind - 1], s[ind]
        self.reverse(s, ind + 1, n)
        
# Approach: This is recursive approach.