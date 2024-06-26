# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        
        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.ans = max(self.ans, left + right + node.val)
            return node.val + max(left, right)
        
        dfs(root)
        return self.ans
    
'''
Approach: Recusive - DFS, & keep updating global ans variable for maximum sum. Since values can be negative,
add left/right subtrees sum only if they are positive.

Check this or any other solution for iterative approach: https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/39927/Iterative-Java-solution
'''
