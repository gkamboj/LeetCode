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
- Return False if there is node (param root) is None, since this means while have reached beyond leaf without reaching target
- If node is leaf node, return result based on targetSum
- Else recursively call for left and right node by subtracting node's sum from targetSum
'''