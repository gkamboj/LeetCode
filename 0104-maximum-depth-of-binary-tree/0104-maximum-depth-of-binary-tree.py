# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack, depth = [root], 0
        while stack:
            depth += 1
            temp = []
            for node in stack:            
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            stack = temp
        return depth
'''
Approach: Iterative - using BFS, update stack with all child nodes at every level and increment depth till
stack is not empty.
'''