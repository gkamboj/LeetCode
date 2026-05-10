# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node): # returns height of subtree rooted at node (distance from node to deepest leaf node)
            if not node:
                return 0
            left = dfs(node.left) # height of left tree
            right = dfs(node.right) # height of right tree
            self.ans = max(self.ans, left + right) # longest path passing through current node - left + right
            return 1 + max(left, right) # height = 1 + max of left and right subtree heights
        
        dfs(root)
        return self.ans

'''
Approach:
Find the height of the left as well as the right part of the tree recursively and take the maximum of those. Refer in-line comments and 
NC video (https://www.youtube.com/watch?v=bkxqA8Rfv04) for details.
'''
