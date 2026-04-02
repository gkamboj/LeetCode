# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        stack, result = [(root, [root.val], targetSum - root.val)], []
        while stack:
            node, path, remaining = stack.pop()
            if not node.left and not node.right and not remaining:
                result.append(path)
            
            if node.left:
                stack.append((node.left, path + [node.left.val], remaining - node.left.val))
            if node.right:
                stack.append((node.right, path + [node.right.val], remaining - node.right.val))
        
        return result

'''
Approach: Similar to LC-112. Keep node, path till now, and remaining sum in the stack. If the popped item
is a leaf node and no sum is remaining, add to the result. Keep doing till all nodes are covered.
'''
