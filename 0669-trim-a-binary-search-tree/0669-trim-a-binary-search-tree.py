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
        if not root:
            return root
        stack = [root]
        while stack:
            curr = stack.pop()
            while curr.left and curr.left.val < low:
                curr.left = curr.left.right
            while curr.right and curr.right.val > high:
                curr.right = curr.right.left
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return root