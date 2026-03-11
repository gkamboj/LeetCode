# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l, r = root.left, root.right
        if (l is None) != (r is None):
            return False
        if not l and not r:
            return True
        s_l, s_r = [l], [r]
        while s_l and s_r:
            curr_l, curr_r = s_l.pop(), s_r.pop()
            if curr_l.val != curr_r.val:
                return False
            if (curr_l.left is None) != (curr_r.right is None):
                return False
            if (curr_l.right is None) != (curr_r.left is None):
                return False
            if curr_l.left:
                s_l.append(curr_l.left)
                s_r.append(curr_r.right)
            if curr_l.right:
                s_l.append(curr_l.right)
                s_r.append(curr_r.left)
        return True
