# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.height(root.left) + self.height(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

'''
Approach: This is a brute force approach.
Diameter of a node is (left_height + right_height + 1). 
Find the diameter of every node and return max of all. This can be done by recursively calling the diameter method for left, right, and
comparing it with diamater of the current node.
'''
