# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack, curr, prev = [], root, -2 **31 - 1
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                temp = stack.pop()
                if temp.val <= prev:
                    return False
                prev = temp.val
                curr = temp.right
        return True
                
'''
Approach: Iterative - inorder DFS template. Maintain previous pointer. During traversal, if the current value is not
greater than the previous at any time, return False. If the while loop completes successfully, return True.
'''
