class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        for row in range(len(land)):
            for col in range(len(land[0])):
                if land[row][col]:
                    ans.append([row, col, row, col])
                    self.dfs(land, row, col, ans)
        return ans
    
    def dfs(self, land, row, col, ans):
        if not 0 <= row < len(land) \
        or not 0 <= col < len(land[0]) \
        or not land[row][col]:
            return
        curr_end_row, curr_end_col = ans[-1][-2], ans[-1][-1]
        if curr_end_row < row or curr_end_col < col:
            ans[-1][-1], ans[-1][-2] = col, row
        land[row][col] = 0
        self.dfs(land, row - 1, col, ans)
        self.dfs(land, row + 1, col, ans)
        self.dfs(land, row, col - 1, ans)
        self.dfs(land, row, col + 1, ans)
            
    
    
'''
Approach: This is advanced version LC-200. Instead of finding just islands, we have to find coordinates also.

'''
        
        