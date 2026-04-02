# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

'''
Approach: 
- Return False if the node (param root) is None, since this means we have reached beyond the leaf without reaching the target.
- If the node is a leaf node, return the result based on the targetSum.
- Else recursively call for the left and right nodes by subtracting the node's sum from targetSum.
'''
