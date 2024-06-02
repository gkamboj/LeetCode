# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        stack = [root]
        while stack:
            curr = stack.pop()
            if self.isSameTree(curr, subRoot):
                return True
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return False
    
    
    def isSameTree(self, node1, node2):
        stack1, stack2 = [node1], [node2]
        while stack1 and stack2:
            curr1, curr2 = stack1.pop(), stack2.pop()
            if not curr1 and not curr2:
                continue
            if not(curr1 and curr2) or curr1.val != curr2.val:
                return False
            stack1.append(curr1.right)
            stack1.append(curr1.left)
            stack2.append(curr2.right)
            stack2.append(curr2.left)
        return True
    
'''
Approach: Iterative - using preorder template for both main function as well as helper (isSameTree) function.
'''
