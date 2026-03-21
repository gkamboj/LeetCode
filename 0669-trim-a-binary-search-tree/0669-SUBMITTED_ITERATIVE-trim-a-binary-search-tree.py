# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        while root and not (low <= root.val <= high):
            if root.val < low:
                root = root.right
            else:
                root = root.left
        
        node = root
        while node:
            while node.left and node.left.val < low:
                node.left = node.left.right
            node = node.left

        node = root
        while node:
            while node.right and node.right.val > high:
                node.right = node.right.left
            node = node.right
        
        return root
        
'''
Approach: 
S-1: Find valid root till current root is out of range. This is to be returned at end.
S-2: Fix left sub tree of the root by going till last level. If, for any iteration,
a node is out of range, assign node's right child to parent's left as the left child
and its further child nodes will be out of range.
S-3: Similar to S-2, fix the right sub tree of root.
'''
