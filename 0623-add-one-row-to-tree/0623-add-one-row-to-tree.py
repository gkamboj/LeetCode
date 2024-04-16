# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        stack = [(root,1)]
        if depth == 1:
            return TreeNode(val, root, None)
        while stack[0][1] + 1 < depth:
            curr, curr_depth = stack.pop(0)
            if curr.left:
                stack.append((curr.left, curr_depth + 1))
            if curr.right:
                stack.append((curr.right, curr_depth + 1))
        while stack:
            curr, _ = stack.pop()
            left = curr.left
            curr.left = TreeNode(val, left, None)
            right = curr.right
            curr.right = TreeNode(val, None, right)
        return root
            