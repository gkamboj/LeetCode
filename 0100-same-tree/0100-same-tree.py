# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1, stack2 = [p], [q]
        while stack1 and stack2:
            curr1, curr2 = stack1.pop(), stack2.pop()
            if not curr1 and not curr2:
                continue
            if not curr1 or not curr2:
                return False
            if curr1.val != curr2.val:
                return False
            stack1.append(curr1.right)
            stack2.append(curr2.right)
            stack1.append(curr1.left)
            stack2.append(curr2.left)
        return not (stack1 or stack2)
    
'''
Approach: Recursive approach -  if both nodes are not null, check revursively for left as well as right sub trees; else return  True if both are null
else False if either is null.

NOTE: Even if inorder and preorder/postorder/levelorder can be used to uniquely identify a tree, that approach will not work here as there are test
cases with duplicate notes. For eg., [1,1] and [1,null,1] will give same inorder and preorder values for both trees even though they are different.
'''