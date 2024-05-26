# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack, depth = [(root, 1)], 0
        while stack:
            node, curr_depth = stack.pop()
            if node:
                depth = max(curr_depth, depth)
                stack.append((node.left, curr_depth + 1))
                stack.append((node.right, curr_depth + 1))
        return depth
'''
Approach: Iterative - using DFS, store node and depth in stack, and keep updating stack with child nodes 
after every pop.
'''