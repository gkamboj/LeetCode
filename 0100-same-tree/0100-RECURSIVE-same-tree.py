# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and\
                self.isSameTree(p.left, q.left) and\
                self.isSameTree(p.right, q.right)
        return p is q
    
'''
Approach: Recursive approach -  if both nodes are not null, check revursively for left as well as right sub trees; else return  True if both are null
else False if either is null.

NOTE: Even if inorder and preorder/postorder/levelorder can be used to uniquely identify a tree, that approach will not work here as there are test
cases with duplicate notes. For eg., [1,1] and [1,null,1] will give same inorder and preorder values for both trees even though they are different.
'''
