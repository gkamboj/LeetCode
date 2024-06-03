# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result, stack, curr = [], [], root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if result and result[-1] >= curr.val:
                    return False
                result.append(curr.val)
                curr = curr.right
        return True
                
'''
Approach: Iterative - inorder template. Before adding to result array, check if value is not greater than last value of result, return False. If while
loop completes successfully, return True.
'''