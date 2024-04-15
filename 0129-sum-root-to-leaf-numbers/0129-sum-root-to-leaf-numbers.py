# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans, stack, val = 0, [(root, str(root.val))], ''
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right:
                ans += int(val)
            if curr.right:
                stack.append((curr.right, val + str(curr.right.val)))
            if curr.left:
                stack.append((curr.left, val + str(curr.left.val)))
        return ans
            
        