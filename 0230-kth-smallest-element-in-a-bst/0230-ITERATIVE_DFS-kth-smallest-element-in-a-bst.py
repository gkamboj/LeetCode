# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack, curr = [], root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                k -= 1
                if not k:
                    return curr.val
                curr = curr.right

'''
Approach: Iterative - inorder template. Decrease k whenever any value is popped from the stack and return vl when k = 0.
'''
