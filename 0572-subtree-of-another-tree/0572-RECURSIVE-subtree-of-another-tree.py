# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    
    def isSameTree(self, node1, node2):
        if node1 and node2:
            return node1.val == node2.val and self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)
        return node1 is node2
    
'''
Approach: Recursive - check if the tree with the current node as the root is the same as the subRoot tree. If not, recursively check for the left as well as the right subtree.

NOTE: Terminating condition returning False works because it's given that the number of nodes will be at least 1 in both nodes. If the minimum nodes were
0, then case with [],[] would have failed. 
'''
