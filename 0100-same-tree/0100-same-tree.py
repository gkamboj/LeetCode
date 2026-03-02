# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            curr_p, curr_q = stack.pop()
            if not curr_p and not curr_q:
                continue
            if not (curr_p and curr_q) or curr_p.val != curr_q.val:
                return False
            stack.extend([(curr_p.left, curr_q.left), (curr_p.right, curr_q.right)])
        return True