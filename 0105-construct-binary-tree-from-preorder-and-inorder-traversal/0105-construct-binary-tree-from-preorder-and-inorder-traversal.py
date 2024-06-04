# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        if not inorder:
            return None
        rootVal = preorder.pop(0)
        inorderIndex = inorder.index(rootVal)
        root = TreeNode(rootVal)
        root.left = self.buildTree(preorder[:inorderIndex], inorder[:inorderIndex])
        root.right = self.buildTree(preorder[inorderIndex:], inorder[inorderIndex + 1:])
        return root
    
        