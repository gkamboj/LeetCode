class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.helper(s, [], 0, result, {})
        return result

    def helper(self, s, vals, ind, result, cache):
        if ind == len(s):
            result.append(list(vals))
            return
        
        for i in range(ind, len(s)):
            if self.isPalindrome(s, ind, i, cache):
                vals.append(s[ind : i + 1])
                self.helper(s, vals, i + 1, result, cache)
                vals.pop()
    
    def isPalindrome(self, s, i, j, cache):
        if (i, j) in cache:
            return cache[(i, j)]
        
        start, end = i, j
        while start <= end:
            if s[start] != s[end]:
                cache[(i, j)] = False
                return False
            start += 1
            end -= 1
        
        cache[(i, j)] = True
        return True

'''
Approach: Backtracking + Memoization (Top-down DP)
- Use DFS to generate all partitions. At each step, try every substring starting at the current index.
- Use a cache (i, j) → True/False to avoid recomputing palindrome checks.
- Only recurse when the substring is a palindrome; build a path and backtrack.

Time: ~O(n² + 2ⁿ)
Space: O(n²) cache + recursion stack.
'''
