# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans, stack = '', [(root, chr(ord('a') + root.val))]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right:
                if not ans: ans = val
                else: ans = min(ans, val)
            if curr.left:
                stack.append((curr.left, chr(ord('a') + curr.left.val) + val))
            if curr.right:
                stack.append((curr.right, chr(ord('a') + curr.right.val) + val))
        return ans
    
'''
Approach: This question is exactly similar to 129. Sum Root to Leaf Numbers. Find the minimum value here
instead of sum.
'''
