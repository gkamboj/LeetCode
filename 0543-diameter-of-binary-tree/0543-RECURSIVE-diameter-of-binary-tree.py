# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left) + 1 # depth of left tree including root (added 1 for root)
            right = dfs(root.right) + 1 # defpth of right tree including root (added 1 for root)
            self.ans = max(self.ans, left + right - 2) # subtracted 2 as diameter will be 2 less than sum of both depths
            return max(left, right)
        
        dfs(root)
        return self.ans
    
'''
Approach: Find depth of left as well as right part of tree (including root) recursively and take maximum of
those less 2 for diameter. Refer in-line comments and NC video (https://www.youtube.com/watch?v=bkxqA8Rfv04) 
for detail.
'''
