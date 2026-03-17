# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder:
            root_val = preorder[0]
            root = TreeNode(root_val)
            ind = inorder.index(root_val)
            root.left = self.buildTree(preorder[1:ind+1], inorder[:ind])
            root.right = self.buildTree(preorder[ind+1:], inorder[ind+1:])
            return root
        return None