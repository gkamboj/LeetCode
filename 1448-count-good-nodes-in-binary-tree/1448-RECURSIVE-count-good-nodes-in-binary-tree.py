# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
    
    def dfs(self, root, maxVal):
        if not root:
            return 0
        ans = 1 if root.val >= maxVal else 0
        ans += self.dfs(root.left, max(root.val, maxVal))
        ans += self.dfs(root.right, max(root.val, maxVal))
        return ans
    
'''
Approach: Recursive - using DFS pre order template.
'''
