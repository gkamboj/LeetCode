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
        return self.helper(root, targetSum, root.val)

    def helper(self, node, targetSum, curr):
        if not node.left and not node.right:
            return curr == targetSum
        elif not node.right:
            return self.helper(node.left, targetSum, curr + node.left.val)
        elif not node.left:
            return self.helper(node.right, targetSum, curr + node.right.val)
        else:
            return self.helper(node.left, targetSum, curr + node.left.val) or self.helper(node.right, targetSum, curr + node.right.val)
        