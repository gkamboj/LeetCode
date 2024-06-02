# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minVal, maxVal = min(p.val, q.val), max(p.val, q.val)
        return self.lcsHelper(root, minVal, maxVal)
    
    def lcsHelper(self, root, minVal, maxVal):
        if minVal <= root.val <= maxVal:
            return root
        elif maxVal > root.val:
            return self.lcsHelper(root.right, minVal, maxVal)
        else:
            return self.lcsHelper(root.left, minVal, maxVal)