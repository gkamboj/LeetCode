# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [0]
        self.helper(root, [k], ans)
        return ans[0]
    
    def helper(self, node, count, ans):
        if node.left:
            self.helper(node.left, count, ans)
        count[0] -= 1
        if not count[0]:
            ans[0] = node.val
            return
        if node.right:
            self.helper(node.right, count, ans)

'''
Approach: Recursive - inorder template. 
'''