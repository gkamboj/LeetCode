# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        if p.val > q.val:
            p, q = q, p
        while not (p.val <= curr.val <= q.val):
            if q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val:
                curr = curr.right
        return curr