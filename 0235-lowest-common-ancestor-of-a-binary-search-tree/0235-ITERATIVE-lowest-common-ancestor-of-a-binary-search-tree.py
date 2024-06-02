# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minVal, maxVal, node = min(p.val, q.val), max(p.val, q.val), root
        while True:
            if minVal <= node.val <= maxVal:
                return node
            elif maxVal > node.val:
                node = node.right
            else:
                node = node.left
        
'''
Approach: Iterative - If root node value is in between both the nodes (inclusive of them), then both nodes are on opposite side of root node, hence 
root node has to be LCS. If not, then go left or right depending on if root node value is smaller or greater than value of both the nodes.
'''
