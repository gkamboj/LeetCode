# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack, ans = [root], []
        while stack:
            temp = []
            right = None
            for node in stack:
                if node:
                    right = node.val
                    temp.append(node.left)
                    temp.append(node.right)
            stack = temp
            if right is not None:
                ans.append(right)
        return ans