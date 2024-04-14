# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans, curr = 0, root
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left:
                if not curr.left.left and not curr.left.right:
                    ans += curr.left.val
                else:
                    stack.append(curr.left)
            if curr.right and (curr.right.left or curr.right.right):
                stack.append(curr.right)
        return ans
