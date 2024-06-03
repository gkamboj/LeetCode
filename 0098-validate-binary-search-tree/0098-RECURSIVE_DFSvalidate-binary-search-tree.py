# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(-(2**31 + 1), root, 2**31)
    
    
    def isValid(self, minBound, node, maxBound):
        if not node:
            return True
        if not (minBound < node.val < maxBound):
            return False
        return self.isValid(minBound, node.left, node.val) and self.isValid(node.val, node.right, maxBound)
                
'''
Approach: Recursive - DFS. Keep minBound and maxBound at every step, which are the just left and just right value encountered till now for the current 
node. For root, take this values as -inf and inf, or ((min possible node.val) - 1) and ((max possible node.val) + 1)
'''
