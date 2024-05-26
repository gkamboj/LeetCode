# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        left, right = root.left, root.right
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root
                
'''
Approach: Recursive code - set result of invertTree for left and right to root.right and root.left 
respectively.
'''
