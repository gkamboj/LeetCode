# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root) != -1
        
    def helper(self, node):
        if not node:
            return 0
        if ((left := self.helper(node.left)) == -1 or
            (right := self.helper(node.right)) == -1 or
            abs(left - right) > 1):
            return -1
        return max(left, right)  + 1
    
    
    
'''
Definition: A tree is height balance if difference of heights of left and right sub tree is at most 1 for 
every node of the tree.

Approach: Bottom-up approach to recursively check the height of left as well as right subtrees for every 
node using DFS.

* NOTE that unlike other submission (using global variable), where left and right are calculated with +1
and return statement is just max(left, right) [without adding 1], here similar approach will fail and we 
have to add 1 at end. This is because here we are modifying the return value in out method itself. Whereas 
other submission was never modifying the return value, so it didn't matter at which step we are adding 1.

* For ITERATIVE approach, refer this link: https://leetcode.com/problems/balanced-binary-tree/discuss/35708/VERY-SIMPLE-Python-solutions-(iterative-and-recursive)-both-beat-90

* Refer NC solution video for detailed theoretical explanation on how this is O(n) slution
'''