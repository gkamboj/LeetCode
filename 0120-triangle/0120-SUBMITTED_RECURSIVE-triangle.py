class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        store = {}
        return self.helper(triangle, 0, 0, store)

    def helper(self, triangle, i, j, store):
        if (key := (i, j)) in store:
            return store[key]

        if i == len(triangle) - 1:
            store[key] = triangle[i][j]
            return store[key]
        
        result = triangle[i][j] + min(self.helper(triangle, i + 1, j, store), self.helper(triangle, i + 1, j + 1, store))
        store[key] = result
        return result

'''
Approach: Use top-down DP (memoization) to recursively compute the minimum path sum.
Cache results for each (i, j) to avoid recomputation of overlapping subproblems and TLE.
'''
