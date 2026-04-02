# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, targetSum - root.val)]
        while stack:
            node, remaining = stack.pop()
            if not node.left and not node.right and not remaining:
                return True
            
            if node.left:
                stack.append((node.left, remaining - node.left.val))
            if node.right:
                stack.append((node.right, remaining - node.right.val))
        
        return False

'''
Approach: Keep a stack to store node as well as remaining sum till node. After every pop, if the
current node is leaf node and no sum is remaining, return True. Else continue. If stack becomes
empty (means all paths have been checked), return False.
'''