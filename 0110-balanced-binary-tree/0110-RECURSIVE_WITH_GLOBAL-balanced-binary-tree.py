# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1
            self.ans = self.ans and abs(right - left) <= 1
            return max(left, right)
        
        dfs(root)
        return self.ans
    
    
'''
Definition: A tree is height balance if difference of heights of left and right sub tree is at most 1 for 
every node of the tree.

Approach: Bottom-up approach to recursively check the height of left as well as right subtrees for every node
using DFS. Maintain a global boolean to check for height balance.

* To avoid global variable, and for ITERATIVE approach, refer this link: https://leetcode.com/problems/balanced-binary-tree/discuss/35708/VERY-SIMPLE-Python-solutions-(iterative-and-recursive)-both-beat-90

* Refer NC solution video for detailed theoretical explanation on how this is O(n) slution
'''
