# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue, depth = [root], 0
        while queue:
            depth += 1
            for _ in range(len(queue)):  
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
        
'''
Approach: Iterative - using BFS, update stack with all child nodes at every level and increment depth till
queue is not empty.

Note: Explore usage deque instead of list
'''
